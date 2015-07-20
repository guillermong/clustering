#!/usr/bin/python

""" argv[1]= carpeta de documetnos para generar clusters
	argv[2]= Numero de clusters deseado
	argv[3]= nivel de compresion
	argv[4]= max cluster size
"""
import os, sys ,getopt
import editdist
import shutil
import distance
import zlib

	
def distancia_zip(s1, s2, nivel=6):
	compressed1 = zlib.compress(s1,nivel)
	compressed2 = zlib.compress(s2,nivel)
	compressed12 = zlib.compress(s1+s2,nivel)

	if len(compressed1) > len(compressed2):
		n = (len(compressed12) - len(compressed2)) / float(len(compressed1))
	else:
		n = (len(compressed12) - len (compressed1)) / float(len(compressed2))	
	return n

		
    
if __name__ == "__main__":
	
	#numero de clusters
	clusters = int(sys.argv[2])
	#doculmentos para generar los clusters
	data=[]  
	#guardar bloque de datos 
	for document in os.listdir(str(sys.argv[1])):
		f = open(str(sys.argv[1])+str(document))
		data.append([f.read()])
		f.close()


	test=[]
	print "sampling cargado, buscando las distancias minimas..."
	for k in range(len(data)):
			for j in range(k+1,len(data)):
				comp=distancia_zip(data[k][0],data[j][0],int(sys.argv[3]))
				print "t1:"+str(k)+" contra t2:"+str(j)+"="+str(comp)
				test.append([comp,data[k][0],data[j][0]])          
	test.sort()
	
	print len(test)	

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
		if cluster2 ==cluster1 or (len(data[cluster1])+len(data[cluster2])) > int(sys.argv[4]) : 
			continue
		test3=data.pop(cluster2)		
		if cluster2<cluster1:
			cluster1-=1
				
		test4=data.pop(cluster1)
		data.append(test3+test4)
		
		densidad=[]		
		print "densididad sampling clster:"+str(test[i][0])
		for t in data:
			densidad.append(len(t))
		print densidad
		
	densidad=[]		
	print "IMPRIMIR DENSIDAD CLUSTER"
	for t in data:
		densidad.append(len(t))
	print densidad
	

	
	for k in range(len(data)):
		division=0
		suma=0		
		for j in range(len(data[k])):
			for i in range(j+1,len(data[k])):
				comp=distancia_zip(data[k][j],data[k][i],int(sys.argv[3]))
				suma+=comp
				division+=1
				#print "t1:"+str(j)+" contra t2:"+str(i)+"="+str(comp)  
		if division == 0:
			division =1  
		print str(k)+"="+str(suma/division)   

	
