#!/bin/sh
export AWS_PAGER=""
export VAULT_ADDR=$VAULT_ADDR
export VAULT_TOKEN=$SSH_TOKEN
vault login --no-print $SSH_TOKEN
export AZ=$NAME
export REGION=$REGION


aws s3api create-bucket --bucket lab-kube.k8s.local --region --region $REGION
aws s3api put-bucket-versioning --bucket lab-kube.k8s.local --versioning-configuration Status=Enabled
aws s3api create-bucket --bucket lab-kops -oidc-store --region $REGION --acl public-read

Create First Cluster:
export CLUSTER_NAME=lab-kube.k8s.local
export KOPS_STATE_STORE=s3://lab-kube.k8s.local
kops create cluster --zones=$NAME ${CLUSTER_NAME}
kops update cluster ${CLUSTER_NAME} --yes




