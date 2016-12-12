#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#Filename:burp_zip.py
#
#Description:use python burp the zip crypt files
#
#Author:rutk1t0r
#
#Date:2016.12.12
#
#GPL
#
#method: the zip file is use cmd:zip -rP 123456 ZIP_TEST.zip exam*
#so the passwd is 123456 ,we can use the example_dictfile to burp crack it

'''
use dictionary file burp crack the zip files
'''
import zipfile
import optparse
import threading

def extractFile(zFile, password):
    try:
        zFile.extractall(pwd = password)

        print("Found Passwd:", password)
        return password

    except:
        pass

def main():
    parser = optparse.OptionParser('Usage%prog -f <zipfile> -d <dictionary>')
    parser.add_option('-f', dest='zname', type='string', help='specify zip file')
    parser.add_option('-d', dest='dname', type='string', help='specify dictionary file')
    option, args=parser.parse_args()
    if option.zname == None or option.dname == None:
        print(parser.usage)
        exit(0)
    else:
        zname = option.zname
        dname = option.dname
    zFile = zipfile.ZipFile(zname)
    dFile = open(dname, 'r')
    for line in dFile.readlines():
        password = line.strip('\n')
        t = threading.Thread(target = extractFile, args = (zFile, password))
        t.start()

if __name__ == '__main__':
    main()
