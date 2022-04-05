Download and install the JAVA agent on the machine from the GUI Console from Getting Strted Area.....

Install Tomcat and Speed Car Racer App

sudo mkdir /opt/appdynamics
cd /opt/appdynamics

sudo git clone https://github.com/Appdynamics/DevNet-Labs.git
sudo curl -O https://archive.apache.org/dist/tomcat/tomcat-7/v7.0.103/bin/apache-tomcat-7.0.103.tar.gz
sudo tar xvzf apache-tomcat-7.0.103.tar.gz
sudo apt -y install build-essential
sudo ./configure
sudo make
sudo make install
