#!/usr/bin/python
import glob
import os,sys
import random

""" argv[1]= carpeta de documentos
	argv[2]= tamano sampling
	argv[3]= carpeta sampling
"""


#lista= glob.glob(str(sys.argv[1])+"*")
print sys.argv[1]
lista=os.listdir(str(sys.argv[1]))
random.seed()

for i in range(int(sys.argv[2])) :
	
		rand = random.randint(0,len(lista))	
		texto= lista.pop(rand)	
		os.rename(sys.argv[1]+texto,sys.argv[3]+texto)
		
print "listo."
