#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
#Filename:tcp_scan.py
#
#Description:use tcp/ip to scan the host port
#
#Author:rutk1t0r
#
#Date:2016.12.12
#
#GPL
#

import optparse, socket
import threading
screenLock = threading.Semaphore(value=1)


def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('thanks\r\n')
        results = connSkt.recv(1024)
        screenLock.acquire()
        print('[+]%d/tcp open' % tgtPort)
        print('[+]'+str(results))
        #connSkt.close()
    except:
        screenLock.acquire()
        print('[-]%d/tcp closed'%tgtPort)
    finally:
        screenLock.release()
        connSkt.close()

def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = socket.gethostbyname(tgtHost)
    except:
        print("[-]Cannot resolve '%s'Unknows host"%tgtHost)
        return
    try:
        tgtName = socket.gethostbyaddr(tgtIP)
        print('\n[+]Scan Results for ' + tgtName[0])
    except:
        print('\n[+]Scan Results for ' + tgtIP)
    socket.setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        print("Scanning port "+str(tgtPort))
        #connScan(tgtHost, int(tgtPort))
        t = threading.Thread(target = connScan, args=(tgtHost, int(tgtPort)))
        t.start()

def main():
    parser = optparse.OptionParser('Usage %prog -H <targethost> -p <targetport>')
    parser.add_option('-H', dest = 'tgtHost', type = 'string', help='specity target host')
    parser.add_option('-p', dest = 'tgtPort', type = 'int', help='specity target port')
    option, args = parser.parse_args()
    tgtHost = option.tgtHost
    tgtPort = option.tgtPort

    if (tgtHost == None) | (tgtPort == None):
        print(parser.usage)
        exit(0)

    args.append(tgtPort)
    #print(args)
    portScan(tgtHost, args)

if __name__ == '__main__':
    main()
    #portScan('www.baidu.com', [80,443,3389,1433,23,445])
