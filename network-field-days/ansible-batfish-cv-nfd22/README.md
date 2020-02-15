# Ansible and Batfish with Arista CloudVision
This is a working example of using Ansible and Batfish to validate network configurations, then send the changes to CloudVision once they are validated.  This was demoed at Network Field Day 22.  The demo flow is as follows:
1. Create configlet to push ACLs with one entry that blocks access to an IP address that should be allowed by uncommenting the following line in `roles/arista/demo/vars/main.yml`:

  # - deny ip any host 158.174.122.199 

2. Show that this IP should be allowed based on assertion in the task:

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

3. Run the playbook (you can use `rundemo.sh`)
4. It should error out and not push the configlet to CV because the host was blocked and shouldn't be
5. Comment the above line and run the playbook again.  This time the assertion should pass, and the configlet will be pushed into CloudVision.  If the configlet already exists you can show that it is modified and the changes are tracked through CloudVision.

