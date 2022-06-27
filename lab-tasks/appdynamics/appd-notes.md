Additional Use Cases and Demos:
===============================
Thousand Eyes and AppD 
https://docs.thousandeyes.com/product-documentation/alerts/integrations/appdynamics-integration
https://developer.thousandeyes.com/v6/alerts/#/integrations


TE & AppD & IWO
================
https://youtu.be/4LGJQ-lBx50


Cool Sox
==============
https://wwwin-github.cisco.com/cx-community/FSO-with-CoolSox

DevNet Sandox
https://devnetsandbox.cisco.com

Integration with AppD:
for this you need to navigate to Alert--> Alert rules--> click/expand the BGP rules--> click on notifications tab-->integration
https://docs.thousandeyes.com/product-documentation/alerts/integrations/appdynamics-integration











**Note do not download the Agent from the SAAS Controller under Servers, instead download it then
complete the conf xml file manually from the main console ***


https://cisco-apipartnertraininglab.saas.appdynamics.com/controller/#/

All Students Must Be Added in here

Link to Download Agents
https://accounts.appdynamics.com/downloads

Install JRE JRE 1.8 is required.
sudo apt-get install procps

https://docs.appdynamics.com/22.1/en/infrastructure-visibility/machine-agent/install-the-machine-agent/linux-install-using-zip-with-bundled-jre


Linux 64 Bit

sudo apt install unzip
sudo apt-get -y install vim

curl -L -O -H "Authorization: Bearer eyJraWQiOiJGemtxZ1A1SDNaa1hVLTZRUDFxcUFtdTFCN1pvSk5FNE52akVSaFNaMG5ZIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULmM3XzJmOVBDak9ES1BVY3ZfaTIzZ25wSDJNcjB6N0VCeFc1MDJWc0hSSlEub2FyMTh5ZmJ6cW9tMzdrZXEycDciLCJpc3MiOiJodHRwczovL2FwcGQtaWRlbnRpdHkub2t0YS5jb20vb2F1dGgyL2F1c3B2bnAzdmtrclNIMk9RMnA2IiwiYXVkIjoibWljb3JzZXJ2aWNlcyIsImlhdCI6MTY0NDIwOTE0MSwiZXhwIjoxNjQ0Mjk1NTQxLCJjaWQiOiIwb2ExanMxMHQ3ekJjTENnRzJwNyIsInVpZCI6IjAwdWVzNmxnMm5xZ0pBdmE0MnA3Iiwic2NwIjpbIm9mZmxpbmVfYWNjZXNzIiwiZG93bmxvYWQiLCJvcGVuaWQiXSwic3ViIjoic2NvbnJvZDFAZ21haWwuY29tIn0.EaR2OOAh2WDtIVbKMFaFMykGUitGtVEwSyezIB-85qChvzAI-uPecRRo4tiVUJHMq6vtGckiHYUpNfKy90FCNDXKalYGyPbL6huGMbOhrYWkcBBKfeXGlQxHs_8PtieqIVlxLHoUtp7yi2xRcqSFubN-ks9VTfVkkgdIe29rQ3hejPBf4UmmTj-AU9ltSUpEVzqWFVhgNPoN464c1Zx5sguEbujeA7DYfBHUmwJVPQ5uDxU2TuJLv6vVoCHVQWwRnk5qguRXw_qbUUaXiSX-ZYo2Q8rr5cYX4X1BTAScWr2to4glX4QNS5RqNuCl4d9Ht84TtvFHgCHTDkRDpd1SRQ;" "https://download.appdynamics.com/download/prox/download-file/netviz-linux/21.3.0.2181/appd-netviz-x64-linux-21.3.0.2181.zip"

unzip appd-netviz-x64-linux-21.3.0.2181.zip
sudo ./install.sh

https://docs.appdynamics.com/22.1/en/infrastructure-visibility/machine-agent/install-the-machine-agent/linux-install-using-zip-with-bundled-jre#

Start the Machine Agent by executing <machine_agent_home>/bin/machine-agent. If you have java or system properties, you can add them to the end of the command. To review machine usage, enter machine-agent -h

Install Service Agent with JRE
https://docs.appdynamics.com/22.1/en/infrastructure-visibility/machine-agent/install-the-machine-agent
https://docs.appdynamics.com/22.1/en/infrastructure-visibility/machine-agent/install-the-machine-agent/linux-install-using-zip-with-bundled-jre

[Support Method to Download the Client
To Download the Client, Logon to the Console, Servers, Download the installer with JRE then you will need to SCP it to the client


Prep - Run Test to Check This
Before Installing Client, check that your instance has enough RAM and CPU
https://docs.appdynamics.com/22.1/en/infrastructure-visibility/machine-agent/machine-agent-requirements-and-supported-environments
Machine Agent >= 21.4.0 collects diskstats from Linux kernels versions >= 4.18.

Check Your Kernel Version:
hostnamectl | grep Kernel

Check your BASH Version:
echo "${BASH_VERSION}"

sudo apt-get install procps

Add an Additional 1 GB of RAM

Check if systemd or sysvinit
pstree -p

Check if this dir exists:
/run/systemd/system

Identify the MachineAgent:
ps -ef | grep machineagent

The supported download installer file doesn't include JRE

So you can download that manually, then copy the conf xml file

Install JRE
sudo apt install default-jre





systemctl start appdynamics-machine-agent






example:
scp -i us-east-2b.yml ~/Downloads/AppServerAgent-21.8.0.32958.zip ubuntu@3.145.73.32:/tmp

Or Curl it down direct:
[This method is not supported by AppD]
https://download-files.appdynamics.com/download-file/machine-bundle/21.4.0.3075/machineagent-bundle-64bit-linux-21.4.0.3075.zip
{This will not be pre-configured for the controller}


TO DO:
See if can get IAM for vault on these machines so that they can make call to vault and get VARS for the controller.xml file
Pass those to ENV VARs then can load them dynamically into the controller.xml file


