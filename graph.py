import networkx as nx
import matplotlib.pyplot as plt
import random as rnd
from friend import friend 

graph_size = (18, 12)

def show_network(network_graph):
    """
    Displays the specified network with associated nodes and edges.
    Args:
        network_graph: A network graph object.
    """
    node_color = [10000.0 * network_graph.degree(v) for v in network_graph]
    pos = nx.spring_layout(network_graph)

    plt.figure(figsize=graph_size)
    nx.draw_networkx(network_graph, pos=pos, with_labels=False,
                    node_color=node_color,
                    node_size=200)
    plt.axis('off')
    plt.show()

#graph = nx.fast_gnp_random_graph(1000, 0.04)
#graph = nx.bull_graph()
graph = nx.erdos_renyi_graph(500, 0.005, seed=123, directed=False)

#print(graph.edges)


show_network(graph)
