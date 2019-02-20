#!/bin/bash

#gps --ndir=$1 --optws --out=`printf %03d $1`_optws.txt

for ((n=2; n<=$1; n++)); do
  gps --ndir=$n --optws --out=`printf %03d $n`_optws.txt
  echo Generated $n directions
done
