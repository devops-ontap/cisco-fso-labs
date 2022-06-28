AppD kubernetes cluster agent is only supported on specific versions of kubernetes:
https://docs.appdynamics.com/4.5.x/en/infrastructure-visibility/monitoring-kubernetes-with-the-cluster-agent/cluster-agent-requirements-and-supported-environments

https://docs.appdynamics.com/22.4/en/infrastructure-visibility/monitor-kubernetes-with-the-cluster-agent/cluster-agent-requirements-and-supported-environments

https://docs.appdynamics.com/22.4/en/infrastructure-visibility/monitor-kubernetes-with-the-cluster-agent/install-the-cluster-agent

https://docs.appdynamics.com/22.4/en/infrastructure-visibility/monitor-kubernetes-with-the-cluster-agent/install-the-cluster-agent/install-the-cluster-agent-with-helm-charts



Here are the links and an example values.yaml file. I don't have a helm chart for an application but I have provided a sample K8s deployment yaml file for a single application service.

https://docs.appdynamics.com/latest/en/infrastructure-visibility/monitor-kubernetes-with-the-cluster-agent/install-the-cluster-agent/install-the-cluster-agent-with-helm-charts
https://docs.appdynamics.com/latest/en/infrastructure-visibility/monitor-kubernetes-with-the-cluster-agent/auto-instrument-applications-with-the-cluster-agent

https://ciscodevnet.github.io/appdynamics-charts/cluster-agent/
https://github.com/CiscoDevNet/appdynamics-charts/blob/master/cluster-agent/values.yaml