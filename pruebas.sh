#!/bin/bash


for i in {1..1}
do

echo 'Obtener muestras:'
python getsampling.py ../sampling/ 9 ../testsampling/


echo 'ejecutar algoritmo de agrupamiento:'


mkdir ../resultados/$i
mkdir ../comprimidos/$i

#python clustering_v3_paralelo.py ../testsampling/ 3 ../resultados/$i/ ../sampling/ 3 9 4 ../comprimidos/$i/
python clustering_v4_paralelo.py ../testsampling/ 3 ../resultados/$i/ ../sampling/ 3 9 4 ../comprimidos/$i/

#python clustering_b.py ../testsampling/ 3 ../resultados/ ../sampling/ 3 9 ../comprimidos/$i/

echo 'regresar muestas:'
python getsampling.py ../testsampling/ 9 ../sampling/ 


#rm -rf ../resultados/*


done
