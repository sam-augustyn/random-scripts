#!/bin/bash

for package in $(pip freeze); do
    name=$(echo $package | sed "s/==.*//")
    pip install $name --upgrade --user
done
