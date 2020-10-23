# Arista vEOS-router Image Import

## vEOS-Router 4.23.5M deployment

1. Open browser to arista.com software download site: <https://www.arista.com/en/support/software-download> (credentials required)
2. browse to image EOS\vEOS-Router\veos-router64-4.23.5M\veos-router64-4.23.5M.qcow2
3. Copy file to eve server using winSCP to \arista (create folder if it doesn't exist)
4. ssh to eve server and execute the following commands:

    ```shell
    cd /arista/
    mv vEOS-Router-4.23.5M.qcow2 hda.qcow2
    mkdir -p /opt/unetlab/addons/qemu/veos-router64-4.23.5M
    mv hda.qcow2 /opt/unetlab/addons/qemu/veos-router64-4.23.5M
    /opt/unetlab/wrappers/unl_wrapper -a fixpermissions
    ```

5. Note: when adding node in EVE-NG topology, for best performance, change the following settings:
   1. CPU: 2
   2. Memory: 4096