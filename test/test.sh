#!/bin/sh

# This script randomly picks an exit code, then returns it.

array[0]=0
array[1]=1
array[2]=127

arraySize=${#array[@]}
arrayIndex=$(($RANDOM % $arraySize))

exit ${array[$arrayIndex]}