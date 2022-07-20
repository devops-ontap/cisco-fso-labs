How to Install Fly
====================

Download the version of fly for your OS.
There is a tiny icon at the bottom right-hand corner of the screen here:
http://ci.devops-ontap.com:8080

MAC & Linux
============
After downloading the fly tool, run these commands:

#sudo mkdir -p /usr/local/bin
#sudo mv ~/Downloads/fly /usr/local/bin
#sudo chmod 0755 /usr/local/bin/fly

If anyone is using Windows ...
If you are using Windows, please install Docker Desktop for Windows and Run fly in a Docker Container 
Corporate Windows Images tend to be hardened or have Group Policies and other software installed that can conflict or cause issues with fly.
It is best in this case to run fly in a docker container

Recording on How To Here:
Webex meeting recording: Windows - Running Fly in Docker
Password: GzuJnTP6
Recording link: https://cisco.webex.com/cisco/ldr.php?RCID=ccfa9c868877c5a146d9016fa31bdfb4

1. Install Docker Desktop
   https://docs.docker.com/get-docker/
2. Start Docker Desktop


docker pull sconrod/ubuntu-fly:latest
docker images -a
docker run -itd imageid
docker ps
docker exec -it containerid

Now you are on the container and you can run fly
Edit your files using vim



