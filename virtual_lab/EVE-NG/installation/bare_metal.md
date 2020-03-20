# EVE-NG Bare Metal Installation

## Pre-Requesits

1. Download Ubuntu Server 16.04.6 LTS: <http://tw.archive.ubuntu.com/ubuntu-cd/16.04/ubuntu-16.04.6-server-amd64.iso>
2. If you need to create bootable USB, follow instruction here:
   1. Windows: <https://tutorials.ubuntu.com/tutorial/tutorial-create-a-usb-stick-on-windows#1>
   2. MAC: <https://tutorials.ubuntu.com/tutorial/tutorial-create-a-usb-stick-on-macos#0>
   3. Or use this tool ISO to USB <https://www.balena.io/etcher/>, works on Linux/Mac and Windows.

## Phase 1 - Ubuntu Server Installation

1. Boot from USB or ISO
2. Select: Install Ubuntu Server
3. Select English
4. Select Location
5. Select Keyboard: (most likley English (US))
6. Select primary network interface
7. Configure Network:
   1. IP Address: x.x.x.x/x
   2. Gateway
   3. Name Server
8. Enter Hostname: EVE-NG-LAB
9. domain name
10. ubuntu archive mirror country: canada
11. select ubuntu archive mirror: ca.archive.ubuntu.com
12. enter proxy if applicable
13. Enter full name of new user
14. enter username
15. enter password
16. Encrypt Home directory: NO
17. Select Timezone
18. Partitioning
    1. Guide - use entire Disk and setup LVM
    2. select disk
    3. select YES remove existing logical data
    4. Select YES to partition disk
    5. use all disk space
    6. write changes to disk - YES
19. Select No automatic updates
20. software to install
    1. standard system utilities
    2. OpenSSH Server
21. install Grub Yes, select bootable device
22. Set clock to UTC
23. remove bootable device and reboot
24. ssh to host and login with user (alt-f1 to see prompt)
25. set root password
    1. `sudo su`
    2. `sudo passwd root`
26. verify hostname and local hosts file, edit as required
    1. `cat /etc/hostname`
    2. `cat /etc/hosts`
27. Edit permissions for root user to allow SSH access to EVE server
    1. `nano /etc/ssh/sshd_config`
    2. Find and edit PermitRootLogin to “yes” => `PermitRootLogin yes`
    3. Confirm edit with ctrl+o followed by enter And ctrl+x for Exit
    4. `sudo service ssh restart`
28. ssh as root to eve server
29. Update the Ubuntu grub CMD Line with the following customized command:
    1. `sed -i -e 's/GRUB_CMDLINE_LINUX_DEFAULT=.*/GRUB_CMDLINE_LINUX_DEFAULT="net.ifnames=0 noquiet"/' /etc/default/grub`
    2. `update-grub`
30. Rename server interface name to eth0
    1. `nano /etc/network/interfaces`
    2. Confirm edit with ctrl+o followed by enter And ctrl+x for Exit, the file should look something like this:

        ```shell
        # The primary network interface
        auto eth0
        iface eth0 inet static
                address 192.168.2.35
                netmask 255.255.255.0
        ```

31. Reboot server
32. note: if system has more then one network interface, it is possible that connectivity is lost after reboot, you will need to do following steps to remap primary adapter to eth0:
    1. `sed -i -e 's/GRUB_CMDLINE_LINUX_DEFAULT=.*/GRUB_CMDLINE_LINUX_DEFAULT="net.ifnames=0 biosdevname=0 noquiet"/' /etc/default/grub`
    2. `update-grub`

## Phase 2 - EVE Pro Installation

1. Start EVE Pro installation `wget -O - http://www.eve-ng.net/repo/install-eve-pro.sh | bash -i`
2. Optional for Broadcom NetExtreme II ethernet drivers: `apt install firmware-bnx2x -o Dpkg::Options::="--force-overwrite"`
3. reboot

## Phase 3 - EVE Pro Setup

1. ssh to server you will be guide through EVE NG setup
2. Enter root password
3. Enter hostname
4. Enter domain name
5. Use static IP
   1. enter managment ip
   2. enter dns domain name
   3. enter ntp server ex: 0.north-america.pool.ntp.org
   4. config proxy setting as required
6. system will reboot
7. ssh to server and apply updates
   1. `apt update` and `apt upgrade`
8. Install eve-ng-dockers
   1. `apt install eve-ng-dockers`
   2. verification after install type `dc images` and should have a display like this:

        ```shell
        root@eve-ng:~# dc images
        REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
        eve-gui-server      latest              a2c79ab18203        6 minutes ago       3.11GB
        eve-wireshark       latest              f8aa7c52f776        19 minutes ago      889MB
        eve-firefox         latest              f14896f741bd        20 minutes ago      1.49GB
        eve-desktop         latest              fc2fb674b7d5        22 minutes ago      2.4GB
        dockergui-rdp       latest              7355d235dc9a        30 minutes ago      553MB
        phusion/baseimage   0.9.22              877509368a8d        2 years ago         225MB
        ```

## Phase 4 - Install License

1. loging to <https://eve-ng.lab> (note: Eve works best with Firefox).
2. Login with default user: admin Password: eve
3. Go to Licensing/License Upload (top of screen) and paste licence
4. verify license - Licensing/License information

Reference:
<https://www.eve-ng.net/images/EVE-COOK-BOOK-1.10.pdf>
