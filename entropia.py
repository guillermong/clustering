#!/usr/bin/python

import os, sys ,getopt
import shutil
import math
 
def Entropy(text):  
    log2=lambda x:math.log(x)/math.log(2)
    exr={}
    infoc=0
    for each in text:
        try:
            exr[each]+=1
        except:
            exr[each]=1
    textlen=len(text)
    print textlen
    for k,v in exr.items():
        freq  =  1.0*v/textlen
        infoc+=freq*log2(freq)
    infoc*=-1
    return infoc
    
todo=""
for document in os.listdir(str(sys.argv[1])):
	f = open(str(sys.argv[1])+str(document))
	texto=f.read()
	todo += texto
print Entropy(todo)
 
