from scapy.all import sniff, TCP, IP

SUSPICIOUS_PORTS = [21]

def detect_suspicious_ports(packet):
    if packet.haslayer(TCP) and packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        src_port = packet[TCP].sport
        dst_port = packet[TCP].dport

        if src_port in SUSPICIOUS_PORTS or dst_port in SUSPICIOUS_PORTS:
            print(f"[!] Suspicious packet detected: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
        else:
            print(f"[+] Normal packet: {src_ip}:{src_port} -> {dst_ip}:{dst_port}")
print("Starting packet sniffing... Press Ctrl+C to stop.")
sniff(filter="tcp", prn=detect_suspicious_ports, store=False,count=10)
