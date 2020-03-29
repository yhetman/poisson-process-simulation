#! /bin/bash
#
#cp poisson_simulation.h /$HOME/include
#
gcc -c -Wall  poisson_simulation.h poisson_simulation.c
if [ $? -ne 0 ]; then
  echo "Compile error."
  exit
fi
#
#mv poisson_simulation.o ~/libc/poisson_simulation.o
#
echo "Normal end of execution."
