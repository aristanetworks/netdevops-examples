# Ansible and Batfish with Arista CloudVision
This is a working example of using Ansible and Batfish to validate network configurations, then send the changes to CloudVision once they are validated.  This was demoed at [Network Field Day 22](https://techfieldday.com/video/arista-devops-day-in-the-life-config-management-and-validation/).  The demo flow is as follows:

## Installation

### Install batfish
```shell
# Configure Python virtual environment
$ virtualenv -p $(which python) .venv
$ source .venv/bin/activate

# Install Python requirements
$ pip install -r requirements.txt

# Install batfish role from galaxy
$ ansible-galaxy install batfish.base

# Start batfish server
$ docker run --name batfish -v batfish-data:/data \
  -p 8888:8888 -p 9997:9997 -p 9996:9996 batfish/allinone
```

### Install CVP Ansible module
```shell
$ ansible-galaxy collection install arista.cvp
```
## Configuration
1. Modify `roles/arista/cv/defaults/main.yml` with the IP address of your CV, and the appropraite credentials.
2. Create entries in your Ansible inventory file, and match those with the entries in `demo.yml`.  

## Demo Workflow

1. Create configlet to push ACLs with one entry that blocks access to an IP address that should be allowed by uncommenting the following line in `roles/arista/demo/vars/main.yml`:

```
  # - deny ip any host 158.174.122.199 
```

2. Show that this IP should be allowed based on assertion in the task:
```
	- name: Assert server can be reached
	  bf_assert:
	    assertions:
	      - type: assert_filter_permits
		name: confirm can access web server
		parameters:
		  filters: demo #'cs-lf12["demo"]'
		  headers:
		    dstIps: '158.174.122.199'
	  delegate_to: localhost
	  run_once: true
```
3. Run the playbook (you can use `rundemo.sh`)

4. It should error out and not push the configlet to CV because the host was blocked and shouldn't be

5. Comment the above line and run the playbook again.  This time the assertion should pass, and the configlet will be pushed into CloudVision.  If the configlet already exists you can show that it is modified and the changes are tracked through CloudVision.

