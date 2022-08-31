# GitHub Audit Tool
This is a tool for auditing github repos, users, and teams. Good for compliance, security and audits.

## Capabilities
* Repo list
* Team list
* Team repo access list

[LICENSE](./LICENSE)

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
