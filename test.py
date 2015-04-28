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
f = open("1mdoc1")
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
print n




