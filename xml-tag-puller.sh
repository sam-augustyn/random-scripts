#!/bin/bash

#pull all the values from the specified xml file ($1)
tags=$(cat $1 | sed -e 's/<\(.*\)>/\1/' | sed 's/>.*//' | awk '{$1=$1};1' | grep -v Response)

#create a unix array, spaces and single quotes around the values
array=$(echo $tags | sed -e "s/ /' '/g")

#print the array to the console
echo "('$array')"
