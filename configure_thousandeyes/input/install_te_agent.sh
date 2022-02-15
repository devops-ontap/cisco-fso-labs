#!/bin/sh
cd input
chmod 400 *.pem
export AWS_PAGER=""
curl -Os https://downloads.thousandeyes.com/agent/install_thousandeyes.sh
chmod +x install_thousandeyes.sh
scp -i *.pem install_thousandeyes.sh


sudo ./insall_thousandeyes.sh -b vojylvcce2gwg4u0e1mcg000gn96h0tj

