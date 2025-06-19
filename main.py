import tkinter as tk
from scanner import scan_network
from visualizer import draw_topology

def start_scan():
    text_output.delete(1.0, tk.END)
    devices = scan_network()
    draw_topology(devices)
    for device in devices:
        text_output.insert(tk.END, f"{device['ip']} - {device['mac']} - {device['hostname']}\n")

# GUI setup
root = tk.Tk()
root.title("Network Topology Visualizer")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

btn_scan = tk.Button(frame, text="Scan Network", command=start_scan)
btn_scan.pack(pady=5)

text_output = tk.Text(frame, height=15, width=60)
text_output.pack()

root.mainloop()
