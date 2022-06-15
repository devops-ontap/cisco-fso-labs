All Dockerfiles used to create the OCI Build Containers and the JAVA Apps Deployed to Kubernetes are 
maintained in a separate repo here:

https://github.com/sconrod-tester/docker-builds

Assoociated Reading
https://opencontainers.org/

A container is a standard unit of software delivery that allows engineering teams to ship software reliably and automatically.

Why is it important to ensure your containers meet OCI standards?
When putting code inside a box and shipping it to various computers, the main concern is that the code should behave in the same way on each platform, be it a developer's laptop, a staging server, or the public cloud. In practice, this is difficult because a software component's dependencies can reach far beyond its code. For example, a Django web application needs the Python code interpreter to run, but may also rely on system libraries, which can be different depending on the operating system.
The code must be packaged with its entire environment to run reliably everywhere. In other words, every single dependency must fit into the application's box.



What is OCI format?
The OCI format is a specification for container images based on the Docker Image Manifest Version 2, Schema 2 format. Container Registry supports pushing and pulling OCI images.

Is Kubernetes OCI-compliant?
As far as Kubernetes is concerned, all OCI-compliant images look the same. Note the following: CRI-O is an implementation of the Kubernetes Container Runtime Interface (CRI), which enables the use of OCI-compatible runtimes. CRI-O can pull your existing Docker images and run them
on your Kubernetes version 1.20 and up.

Each OCI build container is created via a pipeline that takes a standard docker image 
and converts it to an OCI format which is what our Pipeline build containers are generated from.

What is an OCI compliant container?
The Open Container Initiative (OCI) is a Linux Foundation project, started in June 2015 by Docker, to design open standards for operating-system-level virtualization (software containers), most importantly Linux containers.

Concourse provides an OCI located here:

Many Pipeline Tools at this time do not provide you with the freedom to build your own OCI buid container
which can lead to limitations on what you can do in your pipelines.

Concourse has no such limitations and therefore, we are able to create OCI build containers
for any OS - Any brand of Linux and Windows.


OCI standards and is part of the Cloud Native Computing Foundation (CNCF). containerd has a highly modularized architecture and an active community that continuously maintains and improves the project.Mar 18, 2021
