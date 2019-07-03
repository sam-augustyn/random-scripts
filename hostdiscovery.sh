#!/bin/bash

sudo nmap -sP -PR $1 | grep report | sed 's/.*(//' | sed 's/).*//' | sed 's/.* //' > $2
