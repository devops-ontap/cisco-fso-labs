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

#Write the Key to the Vault
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
vault login --no-print $SSH_TOKEN
#vault kv put concourse/main/lab-kops-test/AccessKeyId
#vault kv put concourse/main/lab-kops-test/SecretAccessKey
#Add the code here which will write the key and secret to the vault

