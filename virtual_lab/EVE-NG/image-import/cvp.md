# Arista Cloud Vision Portal (Linux) Image Import

## CVP 2020.2.1

1. Open browser to arista.com software download site: <https://www.arista.com/en/support/software-download> (credentials required)
2. browse to image and download \CloudVision\CloudVision Portal\Active Releases\2019.1\2020.2.1\cvp-2020.2.1-kvm.tgz
3. Copy file to eve server using winSCP to \arista (create folder if it doesn't exist)
4. ssh to eve server and execute the following commands:

    ```shell
    cd /arista/
    mkdir /arista/cvp-2020.2.1
    tar -xvf cvp-2020.2.1-kvm.tgz -C /arista/cvp-2020.2.1/
    mkdir -p /opt/unetlab/addons/qemu/linux-cvp-2020.2.1
    mv /arista/cvp-2020.2.1/disk1.qcow2 /opt/unetlab/addons/qemu/linux-cvp-2020.2.1/hda.qcow2
    mv /arista/cvp-2020.2.1/disk2.qcow2 /opt/unetlab/addons/qemu/linux-cvp-2020.2.1/hdb.qcow2
    /opt/unetlab/wrappers/unl_wrapper -a fixpermissions
    ```

2. Note: when adding node in EVE-NG topology, change the following settings:
   1. CPU: 8
   2. Memory: 24576
   3. Ethernets: 1 or 2
   4. Console change type type from `vnc` to `telnet`
