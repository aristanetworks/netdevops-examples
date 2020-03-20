# Arista vEOS-router Image Import

## vEOS-Router 4.23.0FX deployment

1. Open browser to arista.com software download site: <https://www.arista.com/en/support/software-download> (credentials required)
2. browse to image EOS\vEOS-Router\vEOS-Router64-4.23.0FX\vEOS-Router64-4.23.0FX.qcow2
3. Copy file to eve server using winSCP to \arista (create folder if it doesn't exist)
4. ssh to eve server and execute the following commands:

    ```shell
    cd /arista/
    mv vEOS-Router64-4.23.0FX.qcow2 hda.qcow2
    mkdir -p /opt/unetlab/addons/qemu/veos-Router64-4.23.0FX
    mv hda.qcow2 /opt/unetlab/addons/qemu/veos-Router64-4.23.0FX
    /opt/unetlab/wrappers/unl_wrapper -a fixpermissions
    ```

5. Note: when adding node in EVE-NG topology, for best performance, change the following settings:
   1. CPU: 2
   2. Memory: 4096
