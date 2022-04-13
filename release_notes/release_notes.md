To Do
======


Transition the AMI IDs into the vault
When AWS deploy occurs, query vault based off the NAME supplied to retrieve the AMI IDs

Transition the GROUP TOKEN to the vault.
From the EC2 instance use the Python module for vault - and the AWS EC2 vault auth to call vault for any VARS.
Currently, unable to set ENV vars in EC2 without using a user-data file which is buggy.

Add in the AWS LAB Delete function - so that an Instructor or  can completely delete their lab env and re-deploy
Consider removing the student ability to completely delete their lab if this becomes a problem.

Consider Creating a separate Team for each Lab User if they are not able to play well together in the shared team environment.
This will require some organizational changes to the vault...
under cisco-fso-labs there will require each branch mount point or path. If mount path, each mount path requires its own policy and then a corresponding 
token for duration of lab.

Single Sign-On- it would be great to have one single sign on for everything. Consider using git for this.

Consider setting up an email server so that instead of students having to have their own email login for Thousand Eyes and AppD gui we just give them
a logon to a temporary email account. Ie) set up an smtp server on the existing lab kubernetes environment. This way end of lab, we just delete and re-create.









