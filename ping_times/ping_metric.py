#!/usr/bin/env python

import logging
from subprocess import Popen, PIPE

logging.basicConfig(filename="ping.log",level=logging.DEBUG, format="%(asctime)s %(message)s")

def main():

    while True:
        cmd = "/sbin/ping -c 1 %s"
        p = Popen(cmd % "google.com", shell=True, stdout=PIPE, stderr=PIPE, close_fds=True)
        temp = p.stdout.read()
        try:
            msg = temp.split("\n")[1]
        except IndexError:
            msg = "NA"

        logging.debug(msg)
        
    
if __name__ == "__main__":
    main()
