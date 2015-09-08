#!/usr/bin/python
import glob
import os,sys
import random
import shutil

""" argv[1]= documentos con los nombres de las muestras
	argv[2]= src
	argv[3]= dst
"""
print sys.argv[1]

f = open(sys.argv[1], 'r')
for line in f:
	#print line.rstrip('\r\n')
	#print (sys.argv[2]+line).rstrip('\r\n')
	#print (sys.argv[3]+line).rstrip('\r\n')
	#shutil.copy(src, dest)
	try:
		shutil.copy((sys.argv[2]+line).rstrip('\r\n'),(sys.argv[3]+line).rstrip('\r\n'))
	except:
		print line.rstrip('\r\n')
		pass

print "listo."
