# CloudVision CI/CD
## Overview
This demonstration walks through a Continuous Integration workflow for network configurations. In this scenario you will make two changes to the network, which will trigger CI, validate the changes, and push them into CloudVision via Ansible CVP.

## Requirements
* Create an account on dmz-gitlab
* Account on cv-staging and access to Arista Demo Cluster
* VS Code or another text editor
* Git
* Slack (optional)
  * Subscribe to aristabd slack group and the #cicd channel: aristabd.slack.com

## Steps
### Demo 1: Validate server reachability after ACL change using Batfish
1. Clone the CloudVision repo : 

2. Open a text editor in the directory
3. Create a new branch to work in
    - CLI using Git
    - Text editor command
3. Open the file: `./networks/configs/acl.cfg`
  - Uncomment the ACL line 320 
  - Save/commit the change
4. Show that we have defined a network policy that will get verified with Batfish to ensure access to a critical server by opening `permit.json`

5. Push the file to the repo using git
6. Observe CI workflow by browsing to the CI/CD -> Pipeline view
  * Slack will also notify of the push
7. (optional) create merge request
8. Fix the acl entry by either commenting it or changing the IP address
9. Commit/push and you will trigger a new pipeline
10. This time create a merge request (MR) by going to either the branches view or the files view and selecting the branch you created. 
11. In the merge request you will see the results of the pipeline testing and can approve and merge into the *master* branch
12. Once merged a new pipeline is triggered to validate again, deploy will be an option, but I suggest waiting until after (Demo 2) to deploy.


## Demo 2: Validate security policies using Open Policy Agent (OPA)
1. From Gitlab, open the infosec group, note that we are able to define policies for the devices from an Infosec perspective by the infosec team.
2. Open the opa-policies project
3. Open `network-policy.rego` - this is a file using OPA to define policy rules. In this case at the end of the file you will see we have a policy that indicates that telent should be shutdown on all devices.
4. Edit the file `configlet.txt` and add configuration to enable telnet
```
management telnet
  no shutdown
```
5. Save / commit / push  - following the same steps as the previous demo. In this case the `testpolicy` stage will fail instead. Remove the offending lines and push it back up to the repot
6. This time after the merge is approved and the Validation stage has passed, click the play button on the Deploy stage. This will push the configlets to CVaaS. Open cv-staging and show the configlets created. They both have a prefix of *DEMO*


## Reset the demo
1. Go back to the CI pipeline and click play on the *Destroy* phase
2. Restore the ACL with a correct/commented ACL 320 if you chose to change the ip rather than just commenting the line out.
3. Make sure there are no open MRs

## Running AVD container:
docker run -v ./avd-demo/:/projects \
                -v /etc/hosts:/etc/hosts ansibleavd ansible-playbook playbooks/dc1-fabric-deploy-cvp.yml

## Resources

## 

## Changelog
## TODO
- [ ] add secret detection to ci yaml
```
include:
  - template: Security/Secret-Detection.gitlab-ci.yml
```
https://docs.gitlab.com/ee/user/application_security/secret_detection/index.html

- [ ] Clean up file structure and remove dead files
- [ ] Clean up rego file
- [ ] Change acl to use avd
- [ ] Change telnet to use avd
- [ ] Change code to generate avd

