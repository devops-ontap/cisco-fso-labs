You have learned how to run the following two tasks separately;

1. Query the vault to get the AppDynamics temporary oath bearer token by using the AppDynamics Secret that was passed to your task build container
via the CI tool integration with vault..

2. The temporary AppDynamics Oath Token was written to the vault 


3. You used this oath token to get a list of the latest beta releases for the AppDyanics machine agents.

Your Challenge is to add one more task set - which will use the same methodology to query any of the other AppDynamics APIS.
Please read through the AppDynamics API online documentation here....

https://docs.appdynamics.com/21.6/en/extend-appdynamics/appdynamics-apis

If your code tests out Ok, please commit it with a comment "Completed AppD Challenge #1"