#!/usr/bin/python

""" argv[1]= carpeta de documetnos para generar clusters
	argv[2]= Numero de clusters deseado
	argv[3]= carpeta guardar clusters
	argv[4]= carpeta de documentos
"""
import os, sys ,getopt
import editdist
import shutil
import distance
import zlib

def comprimir( ):
	for i in os.listdir(str(sys.argv[3])):
		os.system('7z a '+i+'.7z '+str(sys.argv[3])+i+'/')
	
def distancia_zip(s1, s2, nivel=6):
	compressed1 = zlib.compress(s1,nivel)
	compressed2 = zlib.compress(s2,nivel)
	compressed12 = zlib.compress(s1+s2,nivel)
	#c1=float(len(compressed1))
	#c2=float(len(compressed2))
	#c12=float(len(compressed12))
	#return float(c12/(c2+c1))
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

	#Crear cluster
	#data=[["asdasdf"],["asdasdg"],["qweqweq"],["qweqwew"],["ghjghjk"],["ghj4hjy"],["gregrec"],["vfetyuj"],["sssssss"],["egergei"]]

	#lista documentos ordenados por sus distancias 
	test=[]
	print "sampling cargado, buscando las distancias minimas..."
	for k in range(len(data)):
			for j in range(k+1,len(data)):
				#comp=editdist.distance(data[k][0],data[j][0])
				#comp=distance.hamming(data[k][0],data[j][0])
				comp=distancia_zip(data[k][0],data[j][0],9)
				print "t1:"+str(k)+" contra t2:"+str(j)+"="+str(comp)
				test.append([comp,data[k][0],data[j][0]])          
	test.sort()
	
	#print "los primeros 10 textos mas pequeos en distancia:"
	#for h in range(20):
	#	print test[h][0]
		
		
		
	print "creando clusters"
	i=0
	while len(data)>1 and len(data) > clusters :
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
		if cluster2 ==cluster1: 
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
		
	
	print "Creando carpetas de clusters..."
	for t in range(len(data)):
		os.mkdir( sys.argv[3]+str(t));

	print "Asignando documentos a los clusters"
	for document in os.listdir(str(sys.argv[4])):
		f = open(str(sys.argv[4])+str(document))
		texto=f.read()
		minimo= 999999
		for j in data:
			for k in range(len(j)):
				#comp=editdist.distance(j[k],texto)
				#comp=distance.hamming(j[k],texto)	
				comp=distancia_zip(j[k],texto,9)		
				if minimo > comp:
					minimo=comp
					cl=data.index(j)

		shutil.copyfile(str(sys.argv[4])+str(document), sys.argv[3]+str(cl)+'/'+str(document))
<<<<<<< HEAD
		#shutil.move(str(sys.argv[4])+str(document), sys.argv[3]+str(cl)+'/'+str(document))		
=======
		#shutil.move(str(sys.argv[4])+str(document), sys.argv[3]+str(cl)+'/'+str(document))				
>>>>>>> d729e42a64c52b05ffd1f69ddafa128084ff1536
		f.close()
	
	comprimir()	
	
	


