# GitHub Audit Tool
This is a tool for auditing github repos, users, and teams. It is useful for compliance, security and auditing of GitHub.

## Capabilities
* Repo list
* Team list
* Team repo rights list
* User list
* User repo rights list

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
    Direct Attached User Rights:
       bfrancom
       jesse-eismgard
       jane-at-eismgard
git://github.com/EISMGard/onetwotest.git 
    Direct Attached User Rights:
       bfrancom
       jesse-eismgard
       jane-at-eismgard
git://github.com/EISMGard/laughing-pancake.git 
    Direct Attached User Rights:
       bfrancom
       jesse-eismgard
       jane-at-eismgard
git://github.com/EISMGard/potential-octo-computing-machine.git 
    Direct Attached User Rights:
       bfrancom
       jesse-eismgard
       jane-at-eismgard
git://github.com/EISMGard/literate-octo-system.git 
    Direct Attached User Rights:
       bfrancom
       jesse-eismgard
       jane-at-eismgard
git://github.com/EISMGard/github-audit-tool.git 
    Direct Attached User Rights:
       bfrancom
       jesse-eismgard
       jane-at-eismgard
git://github.com/EISMGard/test.git 
    Direct Attached User Rights:
       bfrancom
       jesse-eismgard
       jane-at-eismgard
git://github.com/EISMGard/foo.git 
    Direct Attached User Rights:
       bfrancom
       jesse-eismgard
       jane-at-eismgard
git://github.com/EISMGard/bar.git 
    Direct Attached User Rights:
       bfrancom
       jesse-eismgard
       jane-at-eismgard
git://github.com/EISMGard/baz.git 
    Direct Attached User Rights:
       bfrancom
       jesse-eismgard
       jane-at-eismgard

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
       bfrancom
       jesse-eismgard
   b-team  Team Members:
       bfrancom
       jesse-eismgard
   bar team  Team Members:
       bfrancom
       jesse-eismgard
   foo team  Team Members:
       bfrancom
       jane-at-eismgard
   gorakTeam  Team Members:
       bfrancom
       jane-at-eismgard

Users and direct access:
       bfrancom
       jane-at-eismgard
       jesse-eismgard
```
