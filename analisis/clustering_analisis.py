#!/usr/bin/python

""" argv[1]= carpeta de documetnos para generar clusters(sampling)
	argv[2]= Numero de clusters deseado
	argv[3]= carpeta guardar clusters
	argv[4]= carpeta de documentos
	argv[5]= max cluster size
	argv[6]= calidad distancia documento 0-9
	argv[7]= Numero de core
	argv[8]= carpeta de resultados comprimidos
"""
import os, sys ,getopt
import shutil
import zlib
from multiprocessing import Pool
from datetime import datetime
from heapq import heapify, heappush, heappop

data=[] 
combinaciones=[]

	
def distancia_zip(s1, s2, nivel=6):
	compressed1 = zlib.compress(s1,nivel)
	compressed2 = zlib.compress(s2,nivel)
	compressed12 = zlib.compress(s1+s2,nivel)
	if len(compressed1) > len(compressed2):
		n = (len(compressed12) - len(compressed2)) / float(len(compressed1))
	else:
		n = (len(compressed12) - len (compressed1)) / float(len(compressed2))	
	return n

def listadistancia(comb):
	k=combinaciones[comb][0]
	j=combinaciones[comb][1]
	comp=distancia_zip(data[k][0],data[j][0],int(sys.argv[6]))
	print "t1:"+str(k)+" contra t2:"+str(j)+"="+str(comp)
	return [comp,data[k][0],data[j][0]]		
	

    
if __name__ == "__main__":
	
	#numero de clusters
	clusters = int(sys.argv[2])
	#num cores
	numprocesos=int(sys.argv[7])
	
	#guardar bloque de datos 
	for document in os.listdir(str(sys.argv[1])):
		f = open(str(sys.argv[1])+str(document))
		data.append([f.read()])
		f.close()

	print "sampling cargado, buscando las distancias minimas..."
	
	for k in range(len(data)):
			for j in range(k+1,len(data)):
				combinaciones.append((k,j))
	pool = Pool(processes=numprocesos)
	test = pool.map(listadistancia, range(len(combinaciones)), len(combinaciones)/numprocesos)
	pool.close()
	pool.join()

	test.sort()
	print len(test)	
	
	sumapr=0
	for pr in test:
		sumapr+=pr[0]
	print "PROMEDIO DE TODOS LOS DOCUMENTOS:"
	print sumapr/len(test)
	
	distancias_ocupadas=[]
		
	print "creando clusters"
	i=0
	while len(data)>1 and len(data) > clusters and i < len(test):
		cluster1=[]
		cluster2=[]
		t1=False
		t2=False
		for j in data:
			if t1 == True and t2 == True :
				break
			for k in range(len(j)):
				if test[i][1] == j[k]:
					t1=True
					cluster1=data.index(j)
				if test[i][2] == j[k]:
					t2= True
					cluster2=data.index(j)
		i=i+1
		if cluster2 ==cluster1 or (len(data[cluster1])+len(data[cluster2])) > int(sys.argv[5]) : 
			continue
		test3=data.pop(cluster2)		
		if cluster2<cluster1:
			cluster1-=1
				
		test4=data.pop(cluster1)
		data.append(test3+test4)
		
		densidad=[]		
		distancias_ocupadas.append(test[i][0])
		print "densididad sampling clster:"+str(test[i][0])
		for t in data:
			densidad.append(len(t))
		print densidad
	

	
	sumas=0
	for t in distancias_ocupadas:
		sumas+=t
	print "PROMEDIO densididad sampling clster(promedio de todos las distancias ocupadas para formar los clusters):"+str(sumas/len(distancias_ocupadas))
	#print sumas/len(distancias_ocupadas)
	
	
	for listadoc in data:
		resultclust=[]
		for doc in  listadoc:
			for testdoc in test:
				if doc == testdoc[1]:
					resultclust.append(testdoc[0])
		print "distancias entre los documentos de un cluster:"+str(resultclust)		
		#print resultclust
		sumaa=0
		for dstclust in resultclust:
			sumaa+=dstclust
		print "PROMEDIO distancias entre los documentos de un cluster"+str(sumaa/len(resultclust))
		#print sumaa/len(resultclust)
		print "MINIMO distancias entre los documentos de un cluster:"+str(min(resultclust))
		#print min(resultclust)
		print "MAXIMO distancias entre los documentos de un cluster:"+str(max(resultclust))
		#print max(resultclust)
		
			