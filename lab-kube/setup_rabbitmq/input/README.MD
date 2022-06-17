Rabbitmq is a deployment that exists most environments handled by Devops.
We are using Rabbitmq in this lab as it has an easy to use load testing tool - perftest
We can generate load and send to rabbitmq and see the results in AppD to some degree.

If we let this perftest run long enough it will 'take out' the pods and the pods will cycle. 
It will also take down rabbitmq pods and they will cycle.
This should translate into some interesting data in AppD.

exec onto the pod for perftest node

Scaling Payload
https://rabbitmq.github.io/rabbitmq-perf-test/stable/htmlsingle/#random-json-payload

Bench Marking RabbitMQ
https://github.com/rabbitmq/rabbitmq-perf-test/blob/main/html/README.md

The perftest kube deploy is from here:
https://gist.github.com/Zerpet/1a106575fe63a4917f2706c592302b72

https://rabbitmq.github.io/rabbitmq-perf-test/stable/htmlsingle/#stopping-perftest

https://www.cloudamqp.com/blog/load-testing-and-performance-measurements-rabbitmq.html

#note - probably want to put this in vault...
==============================================
export uri=amqp://user:CHANGEME@aa14d42c45b2e42aa9249bd82a422a26-1471557648.us-east-2.elb.amazonaws.com:5672
[Remember, if you want to change rabbitmq password you need to delete the PVC]

Run any perfest...example:

bin/runjava com.rabbitmq.perf.PerfTest --uri $uri --consumers 10 --producers 5 --autoack
[Running this for about 15 minutes will kill pods]

-x 1 -y 2 -u "throughput-test-4" --id "test 4" -s 4000





