#!/usr/bin/env python
"""shebang line to run the script with python3"""

# Written by Ben Francom (benfran.com)
# for EISMGard LLC (eismgard.com) under the MIT License

import csv
import sys
from datetime import datetime
from pathlib import Path
import re
import requests_cache
from decouple import config
from github import Github


# environment variables
CSV_PATH = config('CSV_PATH', default='csv')
TTL = config('TTL', default=3600, cast=int)
OUTPUT_MODE = config('OUTPUT_MODE', default='stdout')

# constants
REPO_URL = "Repository URL"

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
    output_mode = OUTPUT_MODE

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


def get_deploy_keys(org):
    """
    Get list of repositories and their deploy keys
    with creation dates
    """
    print("Getting repo deploy keys...")
    repo_deploy_keys = {}
    for repo in org.get_repos():
        keys = repo.get_keys()
        if keys.totalCount > 0:
            repo_deploy_keys[repo.git_url] = [
                {"key_title": key.title,
                 "key": key.key,
                 "created_at": key.created_at} for key in keys
            ]
    return repo_deploy_keys


def print_output(title, data):
    """Print output to stdout"""
    print(f"\n{title}:")
    if isinstance(data, list):
        print_list(data, indent=2)
    elif isinstance(data, dict):
        print_dict(data, indent=2)


def print_list(data, indent=0):
    """Print list items with indentation"""
    for item in data:
        if isinstance(item, dict):
            print_dict(item, indent + 2)
        else:
            print(f"{' ' * indent}{item}")


def print_dict(data, indent=0):
    """Print dictionary items with indentation"""
    for key, value in data.items():
        print(f"{' ' * indent}{key}")
        if isinstance(value, list):
            print_list(value, indent + 2)
        else:
            print(f"{' ' * (indent + 2)}{value}")


def to_snake_case(string):
    """Convert a string to snake_case"""
    return re.sub(r'[^\w]', '_', string).lower()


def format_value(value):
    """Format a value for CSV output"""
    if isinstance(value, datetime):
        return value.isoformat()
    return str(value)


def generate_rows(data):
    """Generate rows from the data"""
    if isinstance(data, list):
        return [[item] for item in sorted(data, key=str.lower)]

    rows = []
    for key, values in data.items():
        if isinstance(values, list):
            for value in values:
                if isinstance(value, dict):
                    rows.append([key] + [format_value(value.get(k, '')) for k in value.keys()])
                else:
                    rows.append([key, value])
        else:
            rows.append([key, values])

    return sorted(rows, key=lambda x: tuple(str(i).lower() for i in x))


def export_to_csv(data, filename, headers):
    """Export data to CSV file with meaningful headers in snake_case"""
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([to_snake_case(header) for header in headers])
        writer.writerows(generate_rows(data))


def main():
    """Main Function"""
    check_github_environment_variables()
    output_mode = check_output_mode()
    org = get_organization(get_github_client())
    fp = CSV_PATH
    data = {
        "Repo List": (repo_list(org), [REPO_URL]),
        "Team List": (team_list(org), ["Team Name", REPO_URL]),
        "Team Membership List": (team_membership(org), ["Team Name", "Member Username"]),
        "Direct Repo Rights": (repo_rights(org), [REPO_URL, "Collaborator Username"]),
        "Repo Deploy Keys": (get_deploy_keys(org), [REPO_URL, "Key Title", "Key", "Created At"]),
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
        sys.exit(0)
