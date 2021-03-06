#!/usr/bin/python

""" argv[1]= carpeta de documetnos para generar clusters
	argv[2]= Numero de clusters deseado
	argv[3]= carpeta guardar clusters
	argv[4]= carpeta de documentos
	argv[5]= max cluster size
	argv[6]= calidad distancia documento 0-9
	argv[7]= carpeta de resultados comprimidos
"""
import os, sys ,getopt
import editdist
import shutil
import distance
import zlib


def get_size(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size

def comprimir( ):
	for i in os.listdir(str(sys.argv[3])):
		os.system('7z a '+i+'.7z '+str(sys.argv[3])+i+'/')
		os.system('7z a ' +str(sys.argv[7])+i+'.7z '+str(sys.argv[3])+i+'/')
	
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
				comp=distancia_zip(data[k][0],data[j][0],int(sys.argv[6]))
				print "t1:"+str(k)+" contra t2:"+str(j)+"="+str(comp)
				test.append([comp,data[k][0],data[j][0]])          
	test.sort()
	
	#print "los primeros 10 textos mas pequeos en distancia:"
	#for h in range(20):
	#	print test[h][0]
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
		if cluster2 ==cluster1 or (len(data[cluster1])+len(data[cluster2])) > int(sys.argv[5]) : 
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
	print "IMPRIMIR CLUSTER"
	for t in data:
		densidad.append(len(t))
	print densidad
	
	print "Creando carpetas de clusters..."
	
	clust_size=[]
	for t in range(len(data)):
		os.mkdir( sys.argv[3]+str(t));
		clust_size.append(0)

	div=get_size(str(sys.argv[4]))/len(data)
		
	i=0
	
	print "Asignando documentos a los clusters"
	for document in os.listdir(str(sys.argv[4])):		
		test2=[]
		f = open(str(sys.argv[4])+str(document))		
		texto=f.read()
		doc_z = len(texto)
		for j in data:
			for k in range(len(j)):
				#comp=editdist.distance(j[k],texto)
				#comp=distance.hamming(j[k],texto)	
				comp=distancia_zip(j[k],texto,int(sys.argv[6]))	
				test2.append([comp,data.index(j)])	          
		test2.sort()
		
		for s in test2:
			if clust_size[s[1]] < div:
				shutil.copyfile(str(sys.argv[4])+str(document), sys.argv[3]+str(s[1])+'/'+str(document))
				clust_size[s[1]]+=doc_z
				#shutil.move(str(sys.argv[4])+str(document), sys.argv[3]+str(s[1])+'/'+str(document))	
				break
		f.close()
	
	for s in clust_size:
		print s
	
	comprimir()	
	
	


