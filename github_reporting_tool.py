#!/usr/bin/env python

# Written by Ben Francom (benfran.com)
# for EISMGard LLC (eismgard.com) under the MIT License

from decouple import config
from github import Github


def check_environment_variables():
    """Check if required environment variables are set"""
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


def get_github_client():
    """Get GitHub client using access token"""
    return Github(config('GITHUB_TOKEN'))


def get_organization(github_client):
    """Get GitHub organization"""
    return github_client.get_organization(config('GITHUB_ORG_NAME'))


def print_repo_list(org):
    """Print list of repositories"""
    print("Repo List:")
    repos = org.get_repos()
    for r in repos:
        print(f"  {r.git_url}")


def print_team_list(org):
    """Print list of teams and their repositories"""
    print("\nTeam List:")
    teams = org.get_teams()
    for t in teams:
        print(f"   {t.name}")
        team_repos = t.get_repos()
        for repo in team_repos:
            print(f"     {repo.git_url}")


def print_team_membership(org):
    """Print list of teams and their members"""
    print("\nTeam Membership List:")
    teams = org.get_teams()
    for t in teams:
        print(f"  {t.name} Team Members:")
        for m in t.get_members():
            print(f"      {m.login}")


def print_repo_rights(org):
    """Print list of repositories and their direct collaborators"""
    print("\nDirect Repo Rights:")
    repos = org.get_repos()
    for r in repos:
        print(f"  {r.git_url}")
        collaborators = r.get_collaborators()
        for c in collaborators:
            print(f"      {c.login}")


def main():
    check_environment_variables()
    github_client = get_github_client()
    org = get_organization(github_client)

    print_repo_list(org)
    print_team_list(org)
    print_team_membership(org)
    print_repo_rights(org)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")
        exit(0)
