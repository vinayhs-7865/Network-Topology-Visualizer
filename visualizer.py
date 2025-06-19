import networkx as nx
import matplotlib.pyplot as plt

def draw_topology(devices):
    G = nx.Graph()
    router_ip = "192.168.1.1"

    G.add_node(router_ip, label="Router")

    for device in devices:
        G.add_node(device["ip"], label=device["hostname"])
        G.add_edge(router_ip, device["ip"])

    pos = nx.spring_layout(G)
    labels = nx.get_node_attributes(G, 'label')

    plt.figure(figsize=(10, 6))
    nx.draw(G, pos, with_labels=True, labels=labels, node_color='skyblue', node_size=1200, font_size=10)
    plt.title("Network Topology Map")
    plt.savefig("network_topology.png")
    plt.show()
