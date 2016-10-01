#!/usr/bin/env python
# coding: utf-8

import time
import subprocess
from send_mail import send_mail_p3


DOMAIN_NAME = "dummy.com"
IPADDR_FILE = "ipaddr"
TO_MAILADDR = "dummy@gmail.com"


def ping_check():
    pass


def check_nslookup(name):
    cmd = "nslookup " + name
    rtn = subprocess.check_output(cmd.split(" ")).decode('utf-8').split("\n")

    for i in range(len(rtn)):
        if name in rtn[i]:
            buf = rtn[i+1].split(' ')
            ipaddr = buf[1]

    return ipaddr


def get_recent_ipaddr():
    with open(IPADDR_FILE, "r") as r:
        return r.read()


def save_recent_ipaddr(ipaddr):
    cmd = "rm " + IPADDR_FILE
    subprocess.call(cmd.split(" "))

    with open(IPADDR_FILE, "w") as w:
        w.write(ipaddr)


def process():
    domain_name = DOMAIN_NAME
    ipaddr_recent = get_recent_ipaddr()

    ping_check()
    ipaddr_now = check_nslookup(domain_name)

    if ipaddr_recent != ipaddr_now: # state change
        send_mail_p3.send_mail("test@dummy.com",
                               TO_MAILADDR,
                               TO_MAILADDR,
                               domain_name + ": " + ipaddr_recent + " -> " + ipaddr_now,
                               domain_name + ": " + ipaddr_recent + " -> " + ipaddr_now
        )

        save_recent_ipaddr(ipaddr_now)


if __name__ == "__main__":
    process()
