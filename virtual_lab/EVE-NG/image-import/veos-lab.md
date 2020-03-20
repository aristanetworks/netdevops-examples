# Arista vEOS-LAB Image Import

## vEOS-lab 4.22.4M deployment

1. Open browser to arista.com software download site: <https://www.arista.com/en/support/software-download> (credentials required)
2. browse to image EOS\Active Releases\4.22\EOS-4.22.4M\vEOS-lab\vEOS-lab\vEOS-lab-4.22.4M.vmdk
3. Copy file to eve server using winSCP to \arista (create folder if it doesn't exist)
4. ssh to eve server and execute the following commands:

    ```shell
    cd /arista/
    /opt/qemu/bin/qemu-img convert -f vmdk -O qcow2 vEOS-lab-4.22.4M.vmdk hda.qcow2
    mkdir -p /opt/unetlab/addons/qemu/veos-4.22.4M-lab
    mv hda.qcow2 /opt/unetlab/addons/qemu/veos-4.22.4M-lab
    /opt/unetlab/wrappers/unl_wrapper -a fixpermissions
    ```

5. Note: when adding node in EVE-NG topology, for best performance, change the following settings:
   1. CPU: 2
   2. Memory: 4096

## vEOS-lab 4.21.9M deployment

1. Open browser to arista.com software download site: <https://www.arista.com/en/support/software-download> (credentials required)
2. browse to image EOS\Active Releases\4.21\EOS-4.21.9M\vEOS-lab\vEOS-lab\vEOS-lab-4.21.9M.vmdk
3. Copy file to eve server using winSCP to \arista (create folder if it doesn't exist)
4. ssh to eve server and execute the following commands:

    ```shell
    cd /arista/
    /opt/qemu/bin/qemu-img convert -f vmdk -O qcow2 vEOS-lab-4.21.9M.vmdk hda.qcow2
    mkdir -p /opt/unetlab/addons/qemu/veos-4.21.9M-lab
    mv hda.qcow2 /opt/unetlab/addons/qemu/veos-4.21.9M-lab
    /opt/unetlab/wrappers/unl_wrapper -a fixpermissions
    ```

5. Note: when adding node in EVE-NG topology, for best performance, change the following settings:
   1. CPU: 2
   2. Memory: 4096

## vEOS-lab 4.20.15M deployment

1. Open browser to arista.com software download site: <https://www.arista.com/en/support/software-download> (credentials required)
2. browse to image EOS\Active Releases\4.20\EOS-4.20.15M\vEOS-lab\vEOS-lab\vEOS-lab-combined-4.20.15M.vmdk
3. Copy file to eve server using winSCP to \arista (create folder if it doesn't exist)
4. ssh to eve server and execute the following commands:

    ```shell
    cd /arista/
    /opt/qemu/bin/qemu-img convert -f vmdk -O qcow2 vEOS-lab-combined-4.20.15M.vmdk hda.qcow2
    mkdir -p /opt/unetlab/addons/qemu/veos-4.20.15M-lab
    mv hda.qcow2 /opt/unetlab/addons/qemu/veos-4.20.15M-lab
    /opt/unetlab/wrappers/unl_wrapper -a fixpermissions
    ```

5. Note: when adding node in EVE-NG topology, for best performance, change the following settings:
   1. CPU: 2
   2. Memory: 4096
