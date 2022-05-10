#!/usr/bin/env python
import json, re, sys, os, json, subprocess, time, logging, requests, urllib3
from subprocess import call, check_output
from requests.structures import CaseInsensitiveDict
urllib3.disable_warnings()


#Import Lab Vars
lab_vars='lab_vars.py'
import lab_vars
from lab_vars import *

#Inject the vault var vals into the ephemeral oci build container

VAULT_ADDR = os.getenv('VAULT_ADDRR')
VAULT_TOKEN = os.getenv('VAULT_TOKEN')


