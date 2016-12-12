#!/usr/bin/env python
# -*- coding:UTF-8 -*-


import crypt,os,sys

def testPass(cryptPass, filename):
    salt = cryptPass[0:2]
    dictfile = open(filename, 'r')
    #dictfile = open('dictionary.txt', 'r')
    for word in dictfile.readlines():
        word = word.strip('\n')
        cryptWord = crypt.crypt(word, saltt)
        if cryptPass == cryptWord:
            print 'Found password' + word
            return

    print 'Password not found'
    return

def main():
    if len(sys.argc) != 3:
        print '[-] Usage:' + str(sys.argv[0]) +' <dictfile>  <password_file>'
        exit(0)
    passfile = open(sys.argv[1], 'r')
    for line in passfile.readlines():
        user = line.split(':')[0]
        cryptPass = line.split(':')[1].strip('')
        print("Cracking Password For:", user)

        testPass(cryptPass, sys.argv[2])

if __name__ == '__main__':
    main()
