#Install kubectl
RUN apk add --no-cache bash
kubectl --version
kops --version