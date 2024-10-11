#!/usr/bin/env python

# Written by Ben Francom (benfran.com)
# for EISMGard LLC (eismgard.com) under the MIT License

import csv
import json
import re
import requests_cache
from decouple import config
from github import Github
from pathlib import Path


# environment variables
CSV_PATH = config('CSV_PATH', default='csv')
TTL = config('TTL', default=3600)

# create csv directory if it doesn't exist
Path(CSV_PATH).mkdir(parents=True, exist_ok=True)

# cache requests for n seconds
requests_cache.install_cache('github_cache', backend='sqlite', expire_after=TTL)


def check_github_environment_variables():
    """Check if required GitHub environment variables are set"""
    github_token = config('GITHUB_TOKEN', default=None)
    github_org_name = config('GITHUB_ORG_NAME', default=None)

    match (github_token, github_org_name):
        case (None, None):
            print("!!! missing both GITHUB_TOKEN and GITHUB_ORG_NAME environment variables !!!")
        case (None, _):
            print("!!! missing GITHUB_TOKEN environment variable !!!")
        case (_, None):
            print("!!! missing GITHUB_ORG_NAME environment variable !!!")
        case _:
            return  # Both variables are set, so we can return without an error

    exit(1)


def check_output_mode():
    """Check and return the output mode"""
    output_mode = config('OUTPUT_MODE', default='stdout')

    if output_mode not in ['stdout', 'csv', 'both']:
        print("!!! invalid OUTPUT_MODE. Must be 'stdout', 'csv', or 'both' !!!")
        exit(1)

    return output_mode


def get_github_client():
    """Get GitHub client using access token"""
    return Github(config('GITHUB_TOKEN'))


def get_organization(github_client):
    """Get GitHub organization"""
    return github_client.get_organization(config('GITHUB_ORG_NAME'))


def repo_list(org):
    """Get list of repositories"""
    print("Getting repositories...")
    return [r.git_url for r in org.get_repos()]


def team_list(org):
    """Get list of teams and their repositories"""
    print("Getting team repositories...")
    teams_data = {}
    for t in org.get_teams():
        teams_data[t.name] = [repo.git_url for repo in t.get_repos()]
    return teams_data


def team_membership(org):
    """Get list of teams and their members"""
    print("Getting team members...")
    teams_members = {}
    for t in org.get_teams():
        teams_members[t.name] = [m.login for m in t.get_members()]
    return teams_members


def repo_rights(org):
    """Get list of repositories and their direct collaborators"""
    print("Getting repo collaborators...")
    repo_collaborators = {}
    for r in org.get_repos():
        repo_collaborators[r.git_url] = [c.login for c in r.get_collaborators()]
    return repo_collaborators


def print_output(title, data):
    """Print output to stdout"""
    print(f"\n{title}:")
    if isinstance(data, list):
        for item in data:
            print(f"  {item}")
    elif isinstance(data, dict):
        for key, value in data.items():
            print(f"  {key}")
            for item in value:
                print(f"    {item}")


def to_snake_case(string):
    """Convert a string to snake_case"""
    # Remove special characters and replace spaces with underscores
    string = re.sub(r'[^\w\s]', '', string)
    string = string.replace(' ', '_')
    # Convert to lowercase and return
    return string.lower()


def export_to_csv(data, filename, headers):
    """Export data to CSV file with meaningful headers in snake_case and sort by repo and username"""
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        snake_case_headers = [to_snake_case(header) for header in headers]
        writer.writerow(snake_case_headers)

        if isinstance(data, list):
            sorted_data = sorted(data, key=lambda x: x.lower())
            writer.writerows([[item] for item in sorted_data])
        elif isinstance(data, dict):
            sorted_data = []
            for key, values in data.items():
                for value in values:
                    sorted_data.append([key, value])

            # Sort by repository URL (column 0) and then by username (column 1), case-insensitive
            sorted_data.sort(key=lambda x: (x[0].lower(), x[1].lower()))
            writer.writerows(sorted_data)


def main():
    check_github_environment_variables()
    output_mode = check_output_mode()
    github_client = get_github_client()
    org = get_organization(github_client)
    fp = CSV_PATH

    data = {
        "Repo List": (repo_list(org), ["Repository URL"]),
        "Team List": (team_list(org), ["Team Name", "Repository URL"]),
        "Team Membership List": (team_membership(org), ["Team Name", "Member Username"]),
        "Direct Repo Rights": (repo_rights(org), ["Repository URL", "Collaborator Username"]),
    }

    if output_mode in ['stdout', 'both']:
        for title, (result, _) in data.items():
            print_output(title, result)

    if output_mode in ['csv', 'both']:
        for title, (result, headers) in data.items():
            export_to_csv(result, f"{fp}/{title.lower().replace(' ', '_')}.csv", headers)

    print("\nFinished successfully!")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)
