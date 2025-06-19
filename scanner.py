from scapy.all import ARP, Ether, srp
import socket

def scan_network(ip_range="192.168.1.0/24"):
    devices = []
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=2, verbose=0)[0]

    for sent, received in result:
        try:
            hostname = socket.gethostbyaddr(received.psrc)[0]
        except:
            hostname = "Unknown"
        devices.append({
            "ip": received.psrc,
            "mac": received.hwsrc,
            "hostname": hostname
        })
    return devices
