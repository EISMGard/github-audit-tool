# GitHub Audit Tool
This is a tool for auditing github repos, users, and teams. Good for compliance, security and audits.

## Capabilities
* Repo list
* Team list
* Team repo access list

[LICENSE](./LICENSE)

## Installation
Please note that you'll need your github org name and to create a github token with access to all repo, team, and user info.

```sh
$ git clone https://github.com/EISMGard/github-audit-tool
$ cd github-audit-tool
$ virtualenv -p python3 venv
$ source venv/bin/activate
$ pip install -r requirements.txt
$ export GITHUB_ORG_NAME=<your github org name>
$ export  GITHUB_TOKEN=<your github token>
$ python github-reporting-tool.py
```

## Example Output
```
Repo List:
   git://github.com/EISMGard/UnstoppableDevOps.git
   git://github.com/EISMGard/onetwotest.git
   git://github.com/EISMGard/laughing-pancake.git
   git://github.com/EISMGard/potential-octo-computing-machine.git
   git://github.com/EISMGard/literate-octo-system.git
   git://github.com/EISMGard/github-audit-tool.git
   git://github.com/EISMGard/test.git

Team List:
    a-team
      git://github.com/EISMGard/test.git
    b-team
      git://github.com/EISMGard/onetwotest.git
      git://github.com/EISMGard/UnstoppableDevOps.git
    bar team
      git://github.com/EISMGard/laughing-pancake.git
    foo team
      git://github.com/EISMGard/literate-octo-system.git
    gorakTeam
      git://github.com/EISMGard/onetwotest.git

Team Membership List:
   a-team  Team Members:
      Name:  Ben Francom , Email:  None , ID:  5726729 , Login:  bfrancom
      Name:  None , Email:  None , ID:  111655783 , Login:  jesse-eismgard
   b-team  Team Members:
      Name:  Ben Francom , Email:  None , ID:  5726729 , Login:  bfrancom
      Name:  None , Email:  None , ID:  111655783 , Login:  jesse-eismgard
   bar team  Team Members:
      Name:  Ben Francom , Email:  None , ID:  5726729 , Login:  bfrancom
      Name:  None , Email:  None , ID:  111655783 , Login:  jesse-eismgard
   foo team  Team Members:
      Name:  Ben Francom , Email:  None , ID:  5726729 , Login:  bfrancom
      Name:  None , Email:  None , ID:  111656116 , Login:  jane-at-eismgard
   gorakTeam  Team Members:
      Name:  Ben Francom , Email:  None , ID:  5726729 , Login:  bfrancom
      Name:  None , Email:  None , ID:  111656116 , Login:  jane-at-eismgard
```
