#Written by Ben Francom (benfran.com) for EISMGard LLC (eismgard.com) under the MIT License
import os
from unicodedata import name
from github import Github

# using an access token
g = Github(os.environ['GITHUB_TOKEN'])
org = g.get_organization(os.environ['GITHUB_ORG_NAME'])

#env cheeck
if os.environ.get('GITHUB_TOKEN') is not None:


#Get list of repos
    print("Repo List:")
repos = org.get_repos()
for r in repos:
    print("  ",r.git_url)

#Get list of teams
print("\nTeam List:")
teams = org.get_teams()
for t in teams:
    print("   ",t.name)


#Get list of teams
print("\nTeam Membership List:")
teams = org.get_teams()
for t in teams:
    print("  ",t.name," Team Members:")
    for m in t.get_members():
        print("      Name: ",m.name,", Email: ",m.email,", ID: ",m.id,", Login: ",m.login)