#!/bin/sh
echo "#!/bin/bash" >> /env.sh
echo "export VAULT_ADDR=http://vault.devops-ontap.com:8200" >> /env.sh
chmod +x /env.sh
/env.sh