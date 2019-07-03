#!/usr/bin/env python3
import subprocess,re
from netaddr import IPAddress

interface = "wlp2s0"
ipaddressRegex = r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b'

process = subprocess.Popen(['ifconfig', interface], stdout=subprocess.PIPE)
stdout = (process.communicate()[0]).decode("utf-8")
results = re.findall(ipaddressRegex, stdout)
netmask = IPAddress(results[1]).netmask_bits()
slash = 2 ** (32 - netmask) - 1
broadcast = IPAddress(results[2])
print(str(broadcast - slash) + '/' + str(netmask))
