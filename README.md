# GitHub Org Audit Tool
This is a tool for auditing github organizations including their repos, users, and teams. It is useful for compliance, security and auditing.

## Capabilities
* Repo list
* Team list
* Team repo rights list
* User list
* User repo rights list

[LICENSE](./LICENSE)

## Installation
Please note that you'll need your github org name and to create a github token with access to all repo, team, and user info.

### Docker Installation
On your host, you'll need to set your environment variables mentioned above.

```sh
export GITHUB_ORG_NAME=<your github org name>
export  GITHUB_TOKEN=<your github token>

#Build Docker Image
docker build --tag github-audit-tool .

#Run Image
docker run --rm -it -e GITHUB_ORG_NAME -e GITHUB_TOKEN github-audit-tool
```

### Local Installation

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
   git://github.com/EISMGard/foo.git
   git://github.com/EISMGard/bar.git
   git://github.com/EISMGard/baz.git

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
       
Direct Repo Rights:
   git://github.com/EISMGard/UnstoppableDevOps.git
       bfrancom
       jesse-eismgard
       jane-at-eismgard
   git://github.com/EISMGard/onetwotest.git
       bfrancom
       jesse-eismgard
       jane-at-eismgard
   git://github.com/EISMGard/laughing-pancake.git
       bfrancom
       jesse-eismgard
       jane-at-eismgard
   git://github.com/EISMGard/potential-octo-computing-machine.git
       bfrancom
       jesse-eismgard
       jane-at-eismgard
   git://github.com/EISMGard/literate-octo-system.git
       bfrancom
       jesse-eismgard
       jane-at-eismgard
   git://github.com/EISMGard/github-audit-tool.git
       bfrancom
       jesse-eismgard
       jane-at-eismgard
   git://github.com/EISMGard/test.git
       bfrancom
       jesse-eismgard
       jane-at-eismgard
   git://github.com/EISMGard/foo.git
       bfrancom
       jesse-eismgard
       jane-at-eismgard
   git://github.com/EISMGard/bar.git
       bfrancom
       jesse-eismgard
       jane-at-eismgard
   git://github.com/EISMGard/baz.git
       bfrancom
       jesse-eismgard
       jane-at-eismgard
```
