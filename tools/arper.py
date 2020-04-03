from scapy.all import *
import os
import sys
import threading
import signal

interface = "en1"
target_ip = "172.16.224.130"
gateway_ip = "172.16.224.2"
packet_count = 1000

conf.iface = interface

conf.verb = 0

print "[*] Setting up %s" % interface


