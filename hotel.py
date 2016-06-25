#!/usr/bin/env python

import os
import time
import random


def check():
    print 'Checking for success'
    time.sleep(20)
    ping_time = '';
    while ping_time == '':
        ping_time = os.popen('ping -c 1 www.google.com | tail -1| awk \'{print $4}\' | cut -d \'/\' -f 2').read();

    if ping_time > 0:
        print 'Pinged google.com time = ' + ping_time
        print 'Connection established'
    else:
        print 'EPIC Fail'


def gather_mac():
    print 'Scanning network for live hosts...' \
          'Make sure you\'re conenctected to Hotel AP'
    fing_cmd = 'timeout 30 fing | grep -o -E \'([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}\''
    mac = os.popen(fing_cmd).read().split()

    return mac


def spoof(mac):
    print 'mac'
    print 'Choosing MAC (Random)...'
    i = random.randint(0, len(mac))
    print i
    new_mac = mac[i]
    print 'New MAC will be: ' + new_mac
    macchanger_cmd = 'macchanger wlan0 --mac=' + new_mac

    print 'Turning off wlan0'
    os.system('nmcli r wifi off')
    time.sleep(10)
    print 'Changing address'
    os.system(macchanger_cmd)
    print 'Turning on wlan0'
    os.system('nmcli r wifi on')
    time.sleep(10)


def main():
    # local_ip = os.popen('hostname -I').read()
    spoof(gather_mac())
    check()

    return


if __name__ == '__main__':
    main()
