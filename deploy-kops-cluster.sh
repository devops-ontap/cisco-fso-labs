#!/bin/sh
export AWS_PAGER=""
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
vault login --no-print $SSH_TOKEN
export AZ=$NAME
export REGION=$REGION
apt-get -y install wget


LAB_KOPS_AWS_KEY_ID=$(vault kv get -field=AccessKeyId concourse/cisco-fso-labs/us-east-2b/lab-kops)
echo $LAB_KOPS_AWS_KEY_ID
LAB_KOPS_AWS_KEY=$(vault kv get -field=SecretAccessKey concourse/cisco-fso-labs/us-east-2b/lab-kops)
echo $LAB_KOPS_AWS_KEY

aws configure set aws_access_key_id $LAB_KOPS_AWS_KEY_ID
aws configure set aws_secret_access_key $LAB_KOPS_AWS_KEY
aws configure set default.region us-east-2

aws sts get-caller-identity --query Account --output text

aws s3api create-bucket --bucket lab-kube.k8s.local --region us-east-2
aws s3api put-bucket-versioning --bucket lab-kube.k8s.local --versioning-configuration Status=Enabled
aws s3api create-bucket --bucket lab-kops -oidc-store --region us-east-2 --acl public-read

#Create First Cluster:
export CLUSTER_NAME=lab-kube.k8s.local
export KOPS_STATE_STORE=s3://lab-kube.k8s.local
kops create cluster --zones=$NAME ${CLUSTER_NAME}
kops update cluster ${CLUSTER_NAME} --yes




