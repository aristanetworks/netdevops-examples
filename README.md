![](https://img.shields.io/badge/Arista-CVP%20Automation-blue) ![](https://img.shields.io/badge/Arista-EOS%20Automation-blue) ![GitHub](https://img.shields.io/github/license/aristanetworks/netdevops-examples)

# Arista Netdevops Examples

## About

This repository is a central place where Arista demos and examples around netdevops methodology.

<p align="center">
    <img src="docs/media/figure-1-arista-automation.png" width="600"/>
</p>

## Available content

### Demo Content

- [__Arista Validated Design__](ansible/avd-evpn-l3ls-1/): Generate EOS EVPN/VXLAN Fabric deployed using CloudVision and with pre/post deployment tests.
- [__Zero Touch Provisioning to EVPN Fabric__](https://github.com/arista-netdevops-community/ansible-avd-cloudvision-demo): Build a complete EVPN/VXLAN fabric using CloudVision and Zero Touch Provisioning process.
- [__Ansible AVD & CVP Transfer of Information__](https://github.com/arista-netdevops-community/ansible-cvp-toi): Content to build a Transfer of Information on Arista Validated Design and Cloudvision collection.
- [__Ansible to sync configlets across CV servers__](ansible/ansible-sync-configlets): Content to synchronize configlets from one CV server to another. Complete documenation is available on our [EOS Central Knowledge base](https://eos.arista.com/synchronising-cloudvision-portal-configlets-with-ansible/)

### Virtual Labs
- [__List of some EVE-NG topologies leveraging vEOS and CV__](virtual_lab/EVE-NG):
- [__L3 Leaf-Spine w/ BGP Unnumbered & EVPN VXLAN__](virtual_lab/EVE-NG/labs/L3LS_Unnumbered_DCI_Type5): full Layer 3 Leaf-Spine fabric in a 2 datacenter setup with BGP Unnumbered and VXLAN/EVPN
- [__NSX-T and EVPN in EVE-NG lab__](virtual_lab/EVE-NG/labs/NSX-T_EVPN_Type-5): Lab to demonstrate integration of Arista EOS running EVPN with Vmware NSX-T integration.

### Webinar & Presentation content

- [__Network Field Days 22__](demo/ansible-batfish-cv-nfd22/): Ansible & Batfish ([NFD22 webpage](https://techfieldday.com/appearance/arista-networks-presents-at-networking-field-day-22/))
- [__Tech Friday March 2020__](demo/tech-friday-march2020/): Lab used during Tech Friday event.
- [__Network Automation with Ansible & Cloudvision - EMEA Webinar April 2020__](demo/emea-2020-ansible-cvp-automation): Build an EVPN/VXLAN Fabric using Ansible & Cloudvision with pot deployment validation using WARD
- [__Network Field Days 22__](demo/ansible-batfish-cv-nfd22/): Ansible & Batfish ([NFD22 webpage](https://techfieldday.com/appearance/arista-networks-presents-at-networking-field-day-22/)).

## License

All examples and demos available in this repository are provided under [Apache License](LICENSE)

# Ask question or report issue

Please open an issue on Github this is the fastest way to get an answer.

# Contribute

Contributing pull requests are gladly welcomed for this repository. If you are planning a big change, please start a discussion first to make sure we’ll be able to merge it.
