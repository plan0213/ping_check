#!/usr/bin/env python
# coding: utf-8

import time
import subprocess
from send_mail import send_mail_p3


DOMAIN_NAME = ""
IPADDR = "None"


def ping_check():
    pass

def ip_check(name):
    cmd = "nslookup " + name
    rtn = subprocess.check_output(cmd.split(" ")).decode('utf-8').split("\n")

    for i in range(len(rtn)):
        if name in rtn[i]:
            buf = rtn[i+1].split(' ')
            ipaddr = buf[1]

    return ipaddr


def process():
    domain_name = DOMAIN_NAME
    ipaddr = IPADDR

    while True:
        ping_check()

        ipaddr_buf = ip_check(domain_name)
        if ipaddr != ipaddr_buf:
            send_mail_p3.send_mail("",
                                "",
                                "",
                                domain_name + ": " + ipaddr + " -> " + ipaddr_buf,
                                domain_name + ": " + ipaddr + " -> " + ipaddr_buf
                            )
        ipaddr = ipaddr_buf
        time.sleep(3600)


if __name__ == "__main__":
    process()
