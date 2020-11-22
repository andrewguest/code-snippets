#!/bin/bash


FILES=/home/andrew/Downloads/psutil-scripts

for file in $FILES
do
  printf "Converting ${file} to Python3...\n"
  2to3 -n -w ${file}
done
