#! /bin/bash

gcc -c -Wall -I poisson_simulation.h poisson_simulation.c
if [ $? -ne 0 ]; then
  echo "Compile error."
  exit
fi
echo "Normal end of execution."
