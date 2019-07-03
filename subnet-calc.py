#!/usr/bin/env python3
import subprocess,re
from netaddr import IPAddress

interface = "wlp2s0"
ipaddressRegex = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

process = subprocess.Popen(['ifconfig', interface], stdout=subprocess.PIPE)
#return an array of the all the matches in the string after its been decoded
results = re.findall(ipaddressRegex, (process.communicate()[0]).decode("utf-8"))
#get the number of 1s in the result
netmask = IPAddress(results[1]).netmask_bits()
#determine the max amount of hostss
slash = 2 ** (32 - netmask) - 1
#get the broadcast address
broadcast = IPAddress(results[2])
#return the slash notation of the network
print(str(broadcast - slash) + '/' + str(netmask))
