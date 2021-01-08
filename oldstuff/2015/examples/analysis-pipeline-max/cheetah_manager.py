#!/usr/bin/env python
import os,sys
import socket
import getpass
import loop

# Are we on the right host machine?
hostname = socket.gethostname()
if not ("psexport" in hostname or "login" == hostname):
    sys.exit("ERROR: Cannot submit jobs from this host. You are logged in to %s but you need to be logged in to psexport or davinci (login node) to simultaneously submit jobs to the queue and communicate with the google spreadsheet." % hostname)

# Read configuration
if len(sys.argv) < 2:
    sys.exit("Usage: cheetah_manager.py cheetah_manager.cfg")

debug = False
if len(sys.argv) >= 3:
    if sys.argv[2] == "DEBUG":
        debug = True

configfilename = sys.argv[1]

print "Gmail login"
password = getpass.getpass()

if debug:
    loop.loop(configfilename,password)
else:
    while True:
        try:
            loop.loop(configfilename,password)
        except:
            print "WARNING: loop() crashed, restarting..."
