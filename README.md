# Network Topology Visualizer (LAN Mapper)

## Description
Scans the local network to detect connected devices and visually maps the network topology using a simple GUI.

## Features
- Device discovery using ARP
- Hostname resolution
- Visual network graph using NetworkX and Matplotlib
- GUI using Tkinter

## How to Run
1. Install required libraries:
```
pip install -r requirements.txt
```

2. Run the tool:
```
sudo python main.py
```

## Requirements
- Python 3.x
- Admin/root access (for scapy ARP scanning)
