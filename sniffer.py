from scapy.all import sniff
from scapy.layers.inet import IP

def packet_callback(packet):
    if packet.haslayer(IP):
        print("Source IP:", packet[IP].src)
        print("Destination IP:", packet[IP].dst)
        print("Protocol:", packet[IP].proto)
        print("-" * 50)

print("Capturing packets... Press Ctrl+C to stop")

sniff(prn=packet_callback, store=False, count=10)