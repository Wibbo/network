import networkx as nx
import matplotlib.pyplot as plt
import random as rnd
from friend import friend 


node_count = 20
min_friends = 1
max_friends = 4 
number_of_iterations = 20

friends = []

g = nx.Graph()

# Add nodes to the network.
for i in range(node_count):
    friends.append(friend(i))   
g.add_nodes_from(friends)

for friend in friends:
    personal_friends = rnd.randint(min_friends, max_friends)
    close_friends = rnd.sample(friends, personal_friends)

    for close_friend in close_friends:
        g.add_edge(friend, close_friend)

nx.draw(g, with_labels=False, font_weight='bold')
plt.show()

friends_have_more_friends = 0

#for _ in range(number_of_iterations):
for person in g:
    # Select a random person from the network and count their friends.
    selected_persons_friends_count = 0
    # random_friend = rnd.choice(friends)
    for neighbours in g.neighbors(person):
        selected_persons_friends_count += 1

    total_friends = 0
    friend_count = 0

    # Loop through all the selected person's friends.
    for friend in g.neighbors(person):

        # Loop through all the friends of each of the selected person's friends.
        for their_friends in g.neighbors(friend):
            friend_count += 1

    average_friends = friend_count/selected_persons_friends_count

    if average_friends > selected_persons_friends_count:
        friends_have_more_friends += 1


print(f'Number of nodes3: {node_count}')
print(f'Friends have more friends {friends_have_more_friends} times out of {node_count}.')
print(f'This equates to {friends_have_more_friends/node_count*100:.1f} percent of the time.')