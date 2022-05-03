#!/bin/bash

Help()
{
   # Display Help
   echo "Specify playbook number to run."
   echo "Example: ./run.sh -n <playbook number>"
   echo
   echo "options:"
   echo "0     runs ansible-playbook playbooks/0_hello_world.yml"
   echo "1     runs ansible-playbook playbooks/1_command.yml"
   echo "2     runs ansible-playbook playbooks/2_facts.yml"
   echo "3     runs ansible-playbook playbooks/3_backup.yml"
   echo "4     runs ansible-playbook playbooks/4_banner.yml"
   echo "5     runs ansible-playbook playbooks/5_deploy.yml"
   echo "6     runs ansible-playbook playbooks/6_validate.yml"
   echo
}

while getopts ":hn:" option; do
   case $option in
      h) # display Help
         Help
         exit;;
      n) # Enter a number
         Number=$OPTARG
            if [ $Number == 0 ];
            then
            echo "ansible-playbook playbooks/0_hello_world.yml"
            ansible-playbook playbooks/0_hello_world.yml
            elif [ $Number == 1 ];
            then
            echo "ansible-playbook playbooks/1_command.yml"
            ansible-playbook playbooks/1_command.yml
            elif [ $Number == 2 ];
            then
            echo "ansible-playbook playbooks/2_facts.yml"
            ansible-playbook playbooks/2_facts.yml
            elif [ $Number == 3 ];
            then
            echo "ansible-playbook playbooks/3_backup.yml"
            ansible-playbook playbooks/3_backup.yml
            elif [ $Number == 4 ];
            then
            echo "ansible-playbook playbooks/4_banner.yml"
            ansible-playbook playbooks/4_banner.yml
            elif [ $Number == 5 ];
            then
            echo "ansible-playbook playbooks/5_deploy.yml"
            ansible-playbook playbooks/5_deploy.yml
            elif [ $Number == 6 ];
            then
            echo "ansible-playbook playbooks/6_validate.yml"
            ansible-playbook playbooks/6_validate.yml
            else
            echo "Sorry, no matching playbook found"
            echo "'./run.sh -h' for help"
            fi;;
     \?) # Invalid option
         echo "Error: Invalid option"
         exit;;
   esac
done
