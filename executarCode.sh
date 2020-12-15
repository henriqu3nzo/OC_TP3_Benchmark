#!/bin/bash

 gcc -O0 not_friendly.c -o not_friendly

 let value=1
 let i=0

 mkdir Execucoes


while [[ $value -lt 1000 ]]; do
	while [[ $i -lt 10 ]]; do
		(sudo perf stat -e cache-references,cache-misses ./not_friendly $value > /dev/null) > out 2>&1 &&  cat out | grep cache >> ./Execucoes/execucao:$value
		echo "Aguarde..."
		let i+=1
	done
		let value+=10
		let i=0
	
done

rm out
echo "************************"
echo "Execução bem sucedida :)"
echo "************************"


 