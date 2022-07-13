This is a list of 'Gotchas'

Google Chrome with Intersight May throw errors for strict MIME checking..

From MAC OS run:
open -n -a /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --args --user-data-dir="/tmp/chrome_dev_test" --disable-web-security


App D Machine Agent Installer:
=================================
The AppD Installer for Machine Agent that works is the rpm that is downloaded from the Main App Dynamics Console (not the student lab)
The token is only good for one hour which means, you must download a new CURL URL within an hour of installing agents.
Currently there is no way to programatically handle this via the API.
Therefore, you need to create some sort of file storage, such as S3. Download the RPM and save it there. Then call this from the pipeline.

PARAMIKO ERROR:
================

When moving from Python 3.6 to 3.8, Paramiko throws the following error, however, it successfully completes the agent installs via SSH:

Traceback (most recent call last):
File "configure_appd_agents.py", line 35, in <module>
con.connect(hostname=device, username=username, allow_agent=False, pkey=key, port=22, timeout=60)
File "/usr/local/lib/python3.8/dist-packages/paramiko/client.py", line 340, in connect
to_try = list(self._families_and_addresses(hostname, port))
File "/usr/local/lib/python3.8/dist-packages/paramiko/client.py", line 203, in _families_and_addresses
addrinfos = socket.getaddrinfo(
File "/usr/lib/python3.8/socket.py", line 918, in getaddrinfo
for res in _socket.getaddrinfo(host, port, family, type, proto, flags):
socket.gaierror: [Errno -2] Name or service not known