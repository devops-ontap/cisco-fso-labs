for s in `cat hostfile` ; do
    echo; echo $s
    ssh -i sshkey.pem ubuntu@"$s" env TE_GROUP=$TE_GROUP
done
