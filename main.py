import networkx as nx
import matplotlib.pyplot as plt
import random as rnd
from friend import friend 


friend_count = 100
min_friends = 1
max_friends = 20

friends = []

g = nx.Graph()

#s = nx.utils.powerlaw_sequence(200, 3.5) #100 nodes, power-law exponent 2.5
#G = nx.expected_degree_graph(s, selfloops=False)

for i in range(friend_count):
    friends.append(friend(i))
    
g.add_nodes_from(friends)


for f in friends:
    personal_friends = rnd.randint(min_friends, max_friends)
    close_friends = rnd.sample(friends, personal_friends)

    for c in close_friends:
        g.add_edge(f, c)

#nx.draw(g, with_labels=False, font_weight='bold')
#plt.show()

count = 0


random_friend = rnd.choice(friends)

for neighbours in g.neighbors(random_friend):
    count += 1

print(f'Random person {random_friend.id} has {count} friends.')

more_friends = 0

for friend in g.neighbors(random_friend):
    friend_count = 0
    for their_friends in g.neighbors(friend):
        friend_count += 1
        
    print(f'Friend {their_friends.id} has {friend_count} friends.')
    if friend_count > count:
        more_friends += 1

print(f'{more_friends} people have more friends than the random person who has {count} friends.')












