import networkx as nx
import matplotlib.pyplot as plt
import random as rnd
from friend import friend 


node_count =12
min_friends = 6
max_friends = 6
generate_random = True
friends = []
graph_size = (18, 12)

generated_nodes =[]

def count_persons_friends(graph, person_node):

    selected_persons_friends_count = 0

    for _ in graph.neighbors(person_node):
        selected_persons_friends_count += 1

    return selected_persons_friends_count

def generate_node_file():
        personal_friends = rnd.randint(min_friends, max_friends)
        



def generate_random_network(net_graph, node_count, friend_list, min_friends, max_friends):
    """
    Generates a random network of connected nodes. Each node is connected to a random set 
    of other nodes - the number of connections lies between min_friends and max_friends.
    Args:
        net_graph: A network graph object.
        node_count: The number of nodes to create.
        friend_list: A list to store friends.
        min_friends: The minimum number of friends for a particular person.
        max_friends: The maximum number of friends for a particular person.
    Returns: A network graph.
    """
    # Add nodes to the network.
    for i in range(node_count):
        net_graph.add_node(i, friend=friend(i))        

    for person in net_graph.nodes:
        friend_count = count_persons_friends(graph, person)
        personal_friends = rnd.randint(min_friends, max_friends)

        if friend_count >= personal_friends:
            break

        close_friends = rnd.sample(list(net_graph.nodes()), personal_friends)
        
        for close_friend in close_friends:
            if friend_count < personal_friends:

                if not net_graph.has_edge(person, close_friend):
                    net_graph.add_edge(person, close_friend)

    return net_graph


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





if not generate_random:
    graph = nx.read_edgelist("facebook_combined.txt", create_using = nx.Graph(), nodetype=int)
else:
    # Generate a random network with node_count nodes.
    graph = nx.Graph()
    graph = generate_random_network(graph, node_count, friends, min_friends, max_friends)

# Display the network graph.
show_network(graph)


friends_have_more_friends = 0

for person in graph:

    selected_persons_friends_count = 0

    for neighbours in graph.neighbors(person):
        selected_persons_friends_count += 1

    total_friends = 0
    friend_count = 0

    # Loop through all the selected person's friends.
    for friend in graph.neighbors(person):

        # Loop through all the friends of each of the selected person's friends.
        for their_friends in graph.neighbors(friend):
            friend_count += 1

    average_friends = friend_count/selected_persons_friends_count

    if average_friends > selected_persons_friends_count:
        friends_have_more_friends += 1


print(f'Number of people: {node_count}')
print(f'Friends of each person on average have more friends {friends_have_more_friends} times out of {node_count}.')
print(f'This equates to {friends_have_more_friends/node_count*100:.1f} percent of the time.')