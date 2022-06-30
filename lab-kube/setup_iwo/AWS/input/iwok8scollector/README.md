# IWO Kubernetes Collector Deploy via Helm Charts

[Helm](https://helm.sh/) is a kubernetes package manager that allows you to more easily manage charts, which are a
way to package all resources associated with an application.  Helm provides a way to package, deploy and update
using simple commands, and provides a way to customize or update parameters of your resources, without the worry of
yaml formatting. For more info see: [Helm: The Kubernetes Package Manager](https://github.com/helm/helm)

To use this method, you will already have a helm client and tiller server installed (if using Helm 2), and are familiar
with how to use helm and chart repositories. Go to [Helm Docs](https://helm.sh/docs/using_helm/%23quickstart-guide)
to get started.

Use the provided Helm Chart to deploy IWO Kubernetes Collector and create the following resources:
1. Create a Namespace or Project (default is "iwo")
1. Service Account and binding to cluster-admin cluster role (default is "iwo-user" with "iwo-all-binding" binding
   using a cluster-admin roleRef)
1. ConfigMap for the IWO Kubernetes Collector to connect to the IWO server
1. Deploy the IWO Kubernetes Collector Pod

Note:
* When deploying the IWO Kubernetes Collector using helm, the user will use charts that will create resources requiring
  cluster admin role.  If Helm 2 is used, then Tiller is required; please
  [Review Tiller and RBAC requirements](https://docs.helm.sh/using_helm/#tiller-and-role-based-access-control).
  Tiller will need to run with an service account that has
  [cluster role access](https://github.com/fnproject/fn-helm/issues/21).
* The IWO Kubernetes Collector image tag used will depend somewhat on your IWO Server version.  Usually they match,
  e.g. Collector version 8.0.1 works with server version 8.0.1.  For more specific mapping, please refer to:
  [Turbonomic (IWO) Server -> kubeturbo (IWO Kubernetes Collector) version](https://github.com/turbonomic/kubeturbo/tree/master/deploy/version_mapping_kubeturbo_Turbo_CWOM.md)
  and review [Releases](https://github.com/turbonomic/kubeturbo/releases).

## Install

To install, the following command consists of the typical values you would specify.  Substitute your environment
values where you see a <>:

Helm 3 (you will need to create the namespace before running the following Helm command):

`helm install <DEPLOYMENT_NAME> <CHARTLOCATION_OR_REPO> --namespace iwo --set iwoServerVersion=<IWO_SERVER_VERSION>
 --set collectorImage.tag=<IWO_KUBERNETES_COLLECTOR_VERSION> --set targetName=<CLUSTER_IDENTIFIER>`

Helm 2:

`helm install --name <DEPLOYMENT_NAME> <CHARTLOCATION_OR_REPO> --namespace iwo
--set iwoServerVersion=<IWO_SERVER_VERSION> --set collectorImage.tag=<IWO_KUBERNETES_COLLECTOR_VERSION>
--set targetName=<CLUSTER_IDENTIFIER>`

Note it is advised to do a dry run first: `helm install --dry-run --debug`

### Values

The following table shows the values exposed which are also seen in the file `values.yaml`, and
values that are default and/or required are noted.

Parameter|Default Value|Required / Opt to Change|Parameter Type
------------ | ------------- | --------------- | -------------
connectorImage.repository|intersight/pasadena|optional|path to connector repo
connectorImage.tag|1.0.9-1|optional|connector image tag
connectorImage.pullPolicy|IfNotPresent|optional|
collectorImage.repository|intersight/kubeturbo|optional|path to collector repo
collectorImage.tag|8.1.3|optional|collector image tag
collectorImage.pullPolicy|IfNotPresent|optional|
iwoServerVersion|8.0|required|number x.y
targetName|"Your_k8s_cluster"|optional but required for multiple clusters|String, how you want to identify your cluster
args.failVolumePodMoves|true|optional, change to false if you want to move pods which have volumes attached; the pod(s) will be down during move|boolean
args.logginglevel|2|optional|number
args.kubelethttps|true|optional, change to false if k8s 1.10 or older|boolean
args.kubeletport|10250|optional, change to 10255 if k8s 1.10 or older|number
args.stitchuuid|true|optional, change to false if IaaS is VMM, Hyper-V|boolean
HANodeDetectors.nodeRoles|"\"master\""|Optional. Used to automate policies to keep nodes of same role limited to 1 instance per ESX host or AZ (starting with 6.4.3+)|regex used, values in quotes & comma separated `"master"` (default),`"worker","app"` etc

## Claim Target

Once the deployed pods are up and running, perform the following procedure to retrieve the device id and the security
token.  They can be used in your Intersight account to claim the Kubernetes target.

1. Port forward the connector:

   `kubectl -n iwo port-forward <ONE_OF_THE_IWO_KUBERNETES_COLLECTOR_POD> -c iwo-k8s-dc 9110`

2. If a proxy is required for your Kubernetes cluster to connect to `intersight.com`, run the following curl command:

   `curl -XPUT http://localhost:9110/HttpProxies -d ‘{“ProxyType”:“Manual”, “ProxyHost”:“<YOUR_PROXY_SERVER>”,
 “ProxyPort”:<YOUR_PROXY_NUMBER>}’`

3. Run the following to retrieve the device id and security token, respectively.  Use them in your Intersight
   account to claim the Kubernetes target, in the same way you would claim a UCS device target or an Intersight assist.

   ```
   $ curl -s http://localhost:9110/DeviceIdentifiers
   [
     {
       "Id": "22284c13-xxxx-yyyy-zzzz-93a14e4de07f"
     }
   ]* Closing connection 0
   ```

   ```
   $ curl -s http://localhost:9110/SecurityTokens
   [
     {
       "Token": "26AEAECCDD67",
       "Duration": 599
     }
   ]* Closing connection 0
   ```

4. If you encountered an error like the following when retrieving the security token, please confirm your cluster's
connectivity to `intersight.com`.
   ```
   {
     "code":"InternalServerError",
     "message":"Internal error while fetching Claim Code",
     "messageId":"",
     "messageParams":null,
     "traceId":"DCxxxxxxxxxxxxxxxxfc9e4de952584049"
   }
   ```

   Here is one way to inspect and confirm the connectivity to `svc.ucs-connect.com`, which is the cloud DNS of
   `intersight.com`.  The output below shows a good connectivity.  In case not connected, please revisit step 2 if
   a proxy is required.

   ```
   $ kubectl -n iwo exec -it <YOUR_IWO_K8S_COLLECTOR_POD> -c iwo-k8s-collector -- curl https://svc.ucs-connect.com
   svc.ucs-connect.com is alive and healthy at 2020-12-05 16:48:30.218096532 +0000 UTC%
   ```

## Update Versions

### Updating IWO Server
When your IWO server has been updated, you will need to update the configMap resource to reflect the new version.
NOTE: You do not need to make this configMap modification if updating to a minor version like 8.0.1 -> 8.0.2, which
will now be automatically handled.  You would only need to make this change if you are making a major change, i.e
going from 8.0.x -> 8.1.x.

1. After the update, obtain the new IWO Server version.
1. You will update the version value - substitute your values for <>:
  `helm upgrade <DEPLOYMENT_NAME> <CHARTLOCATION_OR_REPO> --namespace iwo --set iwoServerVersion=
   <NEW_IWO_SERVER_VERSION>`
1. Insure the IWO Kubernetes Collector pod restarted to pick up new value
1. Repeat for every kubernetes / OpenShift cluster with an IWO Kubernetes Collector pod

### Updating IWO Kubernetes Collector Image
You may be instructed to update the IWO Kubernetes Collector pod image.  Typically, you can use the same version as
the IWO server, e.g. 8.0.1 and 8.0.2.  We will publish any mapping that is not typical.

1. You will update the `collectorImage.tag` parameter to set a new version. Substitute your values for <>:
  `helm upgrade <DEPLOYMENT_NAME> <CHARTLOCATION_OR_REPO> –namespace iwo –set collectorImage.tag=<NEW_IWO_KUBERNETES_COLLECTOR_VERSION>`
1. Check for changes in configMap parameters to determine if it is better to redeploy.
1. Use collectorImage.pullPolicy of “Always” if the image location and tag have not changed, to force the newer
 image to be pulled. Default value is “IfNotPresent”.
1. Insure IWO Kubernetes Collector pod redeployed with new image
1. Repeat for every kubernetes / OpenShift cluster with an IWO Kubernetes Collector pod
