#!/bin/bash
/usr/local/bin/python3 -m pip install --upgrade pip
apt-get -y install libcurl4-gnutls-dev libexpat1-dev gettext libz-dev libssl-dev openssl-devel
apt -y install git
pip3 install pycurl
python3 -m pip install requests
git clone git://github.com/psf/requests.git
cd requests
python -m pip install .
cd ../
chmod a+x te_api.sh
python3 te_api_get_agents.py



