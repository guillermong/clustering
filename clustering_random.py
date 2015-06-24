#!/usr/bin/python
import glob
import os,sys
import random
import shutil

""" argv[1]= carpeta de documentos
	argv[2]= n clusters
	argv[3]= carpeta resultados
"""


#lista= glob.glob(str(sys.argv[1])+"*")
print sys.argv[1]
lista=os.listdir(str(sys.argv[1]))
random.seed()
print len(lista)


print "Creando carpetas de clusters..."
	
for t in range(int(sys.argv[2])):
	os.mkdir( sys.argv[3]+str(t));

div=len(lista)/int(sys.argv[2])
print div



for i in range(int(sys.argv[2])) :
	for j in range(div) :	
		rand = random.randint(0,len(lista)-1)	
		texto= lista.pop(rand)	
		shutil.copyfile( sys.argv[1]+texto , sys.argv[3]+str(i)+"/"+texto)
		#os.rename(sys.argv[1]+texto,sys.argv[3]+str(i)+"/"+texto)
		
print "listo."
