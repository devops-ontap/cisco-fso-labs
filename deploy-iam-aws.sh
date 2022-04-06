#!/bin/sh
export AWS_PAGER=""
aws iam create-group --group-name lab-kops-test
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AmazonEC2FullAccess --group-name lab-kops-test
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AmazonRoute53FullAccess --group-name lab-kops-test
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess --group-name lab-kops-test
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/IAMFullAccess --group-name lab-kops-test
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AmazonVPCFullAccess --group-name lab-kops-test
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AmazonSQSFullAccess --group-name lab-kops-test
aws iam attach-group-policy --policy-arn arn:aws:iam::aws:policy/AmazonEventBridgeFullAccess --group-name lab-kops-test
aws iam create-user --user-name lab-kops-test
aws iam add-user-to-group --user-name lab-kops-test --group-name lab-kops-test
aws iam create-access-key --user-name lab-kops-test

#Here need the python to get the response from the AWS API in Python
#Set the variables for the new AWS key and Secret and write to the vault
#for now set this manually.
#We need this in order to deploy the kube cluster via kops

#Write the Key to the Vault
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
vault login --no-print $SSH_TOKEN
vault kv put concourse/main/us-east-2b/lab-kops-test/AccessKeyId
#vault kv put concourse/main/$NAME/lab-kops-test/AccessKeyId
vault kv put concourse/main/us-east-2b/lab-kops-test/SecretAccessKey
#vault kv put concourse/main/$NAME/lab-kops-test/SecretAccessKey
#Add the code here which will write the key and secret to the vault
LAB_KOPS_AWS_KEY_ID=$(vault kv get -field=token concourse/main/us-east-2b/lab-kops-test/AccessKeyId)
LAB_KOPS_AWS_KEY=$(vault kv get -field=token concourse/main/us-east-2b/lab-kops-test/SecretAccessKey)

aws configure set aws_access_key_id $LAB_KOPS_AWS_KEY_ID
aws configure set aws_secret_access_key $LAB_KOPS_AWS_KEY
aws configure set default.region us-east-2

aws s3api create-bucket --bucket lab-kube.k8s.local --region --region us-east-2
aws s3api put-bucket-versioning --bucket lab-kube.k8s.local --versioning-configuration Status=Enabled
aws s3api create-bucket --bucket lab-kops -oidc-store --region us-east-2 --acl public-read

Create First Cluster:
export CLUSTER_NAME=lab-kube.k8s.local
export KOPS_STATE_STORE=s3://lab-kube.k8s.local
kops create cluster --zones=$NAME ${CLUSTER_NAME}
kops update cluster ${CLUSTER_NAME} --yes


