#!/usr/bin/python
import glob
import os
import editdist
import sys
import editdist
import zlib

#print str(sys.argv[1])

#print os.listdir("doclust/")
"""while i<n :   
    f = open(os)
    data.append(f.read())
    print data[i]
    i+=1
    f.close()
data=[]    
for document in os.listdir(sys.argv[1]):
	f = open(sys.argv[1]+document)
	data.append(f.read())
print data"""
#os.rename("documents/2","clusters/0/2")

#print sys.argv[2]+str(0)+"/"+str(2)	
#print str(sys.argv[1])+str(2)

#os.rename(str(sys.argv[1])+str(2),sys.argv[2]+str(0)+"/"+str(2))
#os.system('ls')
"""f = open("1mdoc1")
t1=f.read()
f = open("1mdoc2")
t2=f.read()
#print editdist.distance(t1,t2)
#print os.stat("doc1").st_size 
#print os.stat("doc2").st_size 

compressed1 = zlib.compress(t1,1)
compressed2 = zlib.compress(t2,1)
compressed12 = zlib.compress(t1+t2,1)



c1=float(len(compressed1))
c2=float(len(compressed2))
c12=float(len(compressed12))
print c1
print c2
print c12
print float(c12/(c2+c1))

if len(compressed1) > len(compressed2):
        n = (len(compressed12) - len(compressed2)) / float(len(compressed1))
else:
        n = (len(compressed12) - len (compressed1)) / float(len(compressed2))
print "otra formula:" 
print n"""
import glob
import os,sys
import random
import distance


""" argv[1]= carpeta de documentos
	argv[2]= n clusters
	argv[3]= carpeta sampling



#lista= glob.glob(str(sys.argv[1])+"*")
print sys.argv[1]
lista=os.listdir(str(sys.argv[1]))
random.seed()
print lista
print len(lista)


print distance.hamming("night", "nacht")
todo="111111111111"
todo+="2222222222"
print todo
"""

from heapq import heapify, heappush, heappop

h = []
heappush(h, ["5eth", 'write code'])
heappush(h, [7, 'release product'])
heappush(h, [7.1, 'release product'])
heappush(h, ["1", 'write spec'])
heappush(h, [1, 'write spec'])
heappush(h, [3, 'create tests'])
dic={}
#print h
test=heappop(h)
dic[test[0]]=test[1]

print dic[1]
print dic

while len(h):
	print heappop(h)


#print heappop(h)
#print heappop(h)
#print heappop(h)
#print heappop(h)
#print heappop(h)

print "diccionario no eta el 543"
if "542" in dic:
	print "yes"
else:
	print "no"




