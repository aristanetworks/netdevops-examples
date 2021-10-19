This is an example of using Batfish to validate datacenter atd-avd intended configs.

Development Environment:

Docker Engine 20.10.7

MacPro MacOS BigSur 11.6

Python v3.8.5 Anaconda

Jupyter Notebook 6.1.4
    - Install Jupyter extensions i.e. Table of Contents which is helpful in navigating through the codes in Notebook.  Instructions on how to install the extensions are found here https://towardsdatascience.com/12-jupyter-notebook-extensions-that-will-make-your-life-easier-e0aae0bd181.

Instructions on how to setup Batfish on your own laptop is located here <https://batfish.readthedocs.io/en/latest/getting_started.html> and copied below for your convenience.

Setup

Installing Batfish and Pybatfish
Getting started with Batfish is easy. First, pull and run the latest allinone Docker container:

docker pull batfish/allinone
docker run --name batfish -v batfish-data:/data -p 8888:8888 -p 9997:9997 -p 9996:9996 batfish/allinone

Then, install Pybatfish using pip:

python3 -m pip install --upgrade pybatfish

Pybatfish requires python 3 and we recommend that you install it in a virtual environment.

Upgrading Batfish and Pybatfish.

In order to upgrade to the latest Docker container, issue these commands on the Batfish server:

docker stop batfish
docker rm batfish
docker pull batfish/allinone
docker run --name batfish -v batfish-data:/data -p 8888:8888 -p 9997:9997 -p 9996:9996 batfish/allinone

To upgrade Pybatfish, use the same command as above:

python3 -m pip install --upgrade pybatfish

We recommend that you upgrade Batfish and Pybatfish together.
