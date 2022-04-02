sudo -E env VAULT_ADDR=http://vault.devops-ontap.com:8200
echo $VAULT_ADDR
VAULT_ADDR=http://vault.devops-ontap.com:8200
VAULT_ADDR='http://vault.devops-ontap.com:8200' sh ./script.sh
vault login -method=aws header_value=vault.devops-ontap.com role=vault
TE_GROUP=$(vault kv get -field=token concourse/cisco-fso-labs/te-group)
echo $TE_GROUP >> ~/.bashrc
sudo curl -Os https://downloads.thousandeyes.com/agent/install_thousandeyes.sh
sudo chmod a+x install_thousandeyes.sh
sudo ./install_thousandeyes.sh -f $TE_GROUP