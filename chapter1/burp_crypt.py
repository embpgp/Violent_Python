#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
#Filename:burp_crypt.py
#
#Description:use python burp crack the password on　Unix-like OS
#
#Author:rutk1t0r
#
#Date:2016.12.11
#
#GPL
#

import crypt,os
import sys

def testPass(cryptPass, dPass):
    salt = cryptPass[0:2]   #salt, only 2 bytes
    dictfile = open(dPass, 'r')
    #dictfile = open('dictionary.txt', 'r')
    for word in dictfile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, salt)
        if cryptPass==cryptWord:
            print 'Found password:' + word
            return

    print 'Password not found'
    return

def main():
    if len(sys.argv) != 3:
        print '[-] Usage:' + str(sys.argv[0]) +' <dictfile>  <password_file>'
        """
        dictfile is like  user:md5_value
        password_file is like 123456
        """
        exit(0)
    passfile = open(sys.argv[2], 'r')
    for line in passfile.readlines():
        user = line.split(':')[0]
        print user
        cryptPass = line.split(':')[1].strip('\n')
        print cryptPass
        print("Cracking Password For:", user)

        testPass(cryptPass, sys.argv[1])

if __name__ == '__main__':
    main()
