#!/bin/sh
i=0
while [ $i -ne 100 ]
do
        i=$(($i+1))
        #echo "$i"
        [ $((i%2)) -eq 1 ] && echo "$i"
done
