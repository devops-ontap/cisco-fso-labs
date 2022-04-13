#!/bin/sh
export AWS_PAGER=""
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
vault login --no-print $SSH_TOKEN
export AZ=$NAME
export REGION=$REGION
apt-get -y install wget

aws sts get-caller-identity --query Account --output text

export AWS_ACCESS_KEY_ID=$(vault kv get -field=AccessKeyId concourse/main/us-east-2b/lab-kops-iam)
export AWS_SECRET_ACCESS_KEY=$(vault kv get -field=SecretAccessKey concourse/main/us-east-2b/lab-kops)

aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
aws configure set default.region us-east-2

aws sts get-caller-identity --query Account --output text

aws s3api create-bucket --bucket lab-kube.k8s.local --region us-east-1
aws s3api put-bucket-versioning --bucket lab-kube.k8s.local --versioning-configuration Status=Enabled
aws s3api create-bucket --bucket lab-kube-oidc -oidc-store --region us-east-1 --acl public-read

#Create First Cluster:
export NAME=lab-kube.k8s.local
export KOPS_STATE_STORE=s3://lab-kube.k8s.local
kops create cluster --zones=us-east-1b $NAME
kops update cluster --name lab-kube.k8s.local --yes --admin


export NAME=lab-kube.k8s.local
export KOPS_STATE_STORE=s3://lab-kube.k8s.local





