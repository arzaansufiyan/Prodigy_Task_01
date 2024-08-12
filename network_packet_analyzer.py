from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP


def packet_handler(packet):
    # Check if the packet has an IP layer
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = packet[IP].proto

        print(f"Source IP: {ip_src} -> Destination IP: {ip_dst}")

        # Check for protocol types
        if proto == 6:  # TCP Protocol
            print("Protocol: TCP")
            if TCP in packet:
                print(f"Source Port: {packet[TCP].sport} -> Destination Port: {packet[TCP].dport}")
        elif proto == 17:  # UDP Protocol
            print("Protocol: UDP")
            if UDP in packet:
                print(f"Source Port: {packet[UDP].sport} -> Destination Port: {packet[UDP].dport}")
        elif proto == 1:  # ICMP Protocol
            print("Protocol: ICMP")

        # Print the payload if available
        if raw in packet:
            print(f"Payload: {packet[Raw].load}")

        print("\n")

# Usage warning
print("Ensure this tool is used ethically and only on networks you have permission to monitor.")

def start_sniffing(interface=None):
    sniff(iface=interface, prn=packet_handler, store=False)

# Start sniffing on the default interface or specify one
if __name__ == "_main_":
    interface = input("Enter the interface to sniff on (or press Enter to sniff on all interfaces): ")
    start_sniffing(interface)
