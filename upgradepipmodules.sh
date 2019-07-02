#!/bin/bash

for package in $(python3 -m pip freeze); do
    name=$(echo $package | sed "s/==.*//")
    python3 -m pip install $name --upgrade --user
done
