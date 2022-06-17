exec onto the pod for perftest

https://rabbitmq.github.io/rabbitmq-perf-test/stable/htmlsingle/#stopping-perftest

https://www.cloudamqp.com/blog/load-testing-and-performance-measurements-rabbitmq.html

export uri=amqp://user:CHANGEME@aa14d42c45b2e42aa9249bd82a422a26-1471557648.us-east-2.elb.amazonaws.com:5672
[Remember, if you want to change rabbitmq password you need to delete the PVC]

Run any perfest...example:

bin/runjava com.rabbitmq.perf.PerfTest --uri $uri --consumers 10 --producers 5 --autoack
[Running this for about 15 minutes will kill pods]



