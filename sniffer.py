from scapy.all import sniff, IP, Raw

def packet_callback(packet):
    # Ensure the packet has an IP layer
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        
        print(f"[*] Protocol: {protocol} | {ip_src} -> {ip_dst}")
        
        # Check for payload data in the Raw layer
        if packet.haslayer(Raw):
            payload = packet[Raw].load
            print(f"    Payload (first 50 bytes): {payload[:50]}")
        
        print("-" * 50)

# Start sniffing on the default interface
# Run this with sudo to allow promiscuous mode
print("Starting packet sniffer... (Press Ctrl+C to stop)")
sniff(filter="ip", prn=packet_callback, store=0)
