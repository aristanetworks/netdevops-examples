# To test out config generation and run in docker:
```
docker run -v /Users/fredlhsu/cicd/network/cloudvision/avd-demo/:/projects -it -w /projects -v /etc/hosts:/etc/hosts fredhsu/avd ansible-playbook playbooks/dc1-fabric-generate.yml
```
Output will be in `/Users/fredlhsu/cicd/network/cloudvision/avd-demo/inventory/intended/configs/`
