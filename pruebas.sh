#!/bin/bash


for i in {1..10}
do

echo 'Obtener muestras:'
python getsampling.py ../../home/gnavarrog/1m/ 40 sampling/

echo 'ejecutar algoritmo de agrupamiento:'


mkdir resultados/$i
mkdir comprimidos/s40_2/$i

#python clustering_v3_paralelo.py ../testsampling/ 3 ../resultados/$i/ ../sampling/ 3 9 4 ../comprimidos/$i/
#python clustering_b.py ../testsampling/ 3 ../resultados/ ../sampling/ 3 9 ../comprimidos/$i/

python clustering_v4_paralelo.py sampling/ 10 resultados/$i/ ../../home/gnavarrog/1m/ 4 9 8 comprimidos/s40_2/$i



echo 'regresar muestas:'
python getsampling.py sampling/ 40 ../../home/gnavarrog/1m/

rm -rf resultados/*

done
