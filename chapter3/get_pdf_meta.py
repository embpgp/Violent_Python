#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
#Filename:get_pdf_meta.py
#
#Description:get meta data from pef file
#
#Author:rutk1t0r
#
#Date:2017.01.15
#
#GPL
#
#pip install pyPdf
#example: wget http://www.wired.com/images_blogs/threatlevel/2010/12/ANONOPS_The_Press_Release.pdf


import pyPdf
from pyPdf import PdfFileReader
import optparse

def printMeta(fileName):
	pdfFile = PdfFileReader(file(fileName, 'rb'))
	docInfo = pdfFile.getDocumentInfo()
	print('[*] PDF MetaData For:' + str(fileName))
	for metaItem in docInfo:
		print('[+]' + metaItem + ':' + docInfo[metaItem])


def main():
	parser = optparse.OptionParser('usage %parg -F<PDF file name>')
	parser.add_option('-F', dest='fileName', type='string',help='specify PDF file name')
	(options, args) = parser.parse_args()
	fileName = options.fileName
	if fileName == None:
		print(parser.usage)
		exit(1)
	else:
		printMeta(fileName)

if __name__ == '__main__':
	main()
