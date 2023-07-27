import networkx as nx
import matplotlib.pyplot as plt
import itertools
import random

import time
start_time = time.time()
print "Timer started"

G=nx.gnp_random_graph(10,0.7)
for (u, v) in G.edges():
    G.edge[u][v]['weight'] = random.randint(0,100)

scenario_total_distance=[]
scenario_num=[]
a=list(itertools.combinations(nx.nodes(G),3))
b=list(itertools.combinations(nx.nodes(G),3))
c=nx.nodes(G)
d=nx.nodes(G)

for i in a:  # Cache Location
	for j in b:  # TRAU lcoation
		distance=0
		for k in c:
			distance += min ((nx.shortest_path_length(G,source=i[0],target=k,weight='weight')),(nx.shortest_path_length(G,source=i[1],target=k,weight='weight')),(nx.shortest_path_length(G,source=i[2],target=k,weight='weight')))
			for l in d:
				distance += min ((nx.shortest_path_length(G,source=k,target=j[0],weight='weight')+nx.shortest_path_length(G,source=j[0],target=l,weight='weight')),(nx.shortest_path_length(G,source=k,target=j[1],weight='weight')+nx.shortest_path_length(G,source=j[1],target=l,weight='weight')),(nx.shortest_path_length(G,source=k,target=j[2],weight='weight')+nx.shortest_path_length(G,source=j[2],target=l,weight='weight')))
		scenario_total_distance.append(distance)
		scenario_num.append(list(i)+list(j))


finali=0
### Print Min Distance Scenarios code
w=min(scenario_total_distance)
for i in range(0,len(scenario_total_distance)):
	if(-0.0001<scenario_total_distance[i]-w<0.0001):
		print (scenario_num[i])
		finali=i
###

print("%s seconds" % (time.time() - start_time))

nx.draw_circular(G,nodelist=list(set(G.nodes())-set(scenario_num[finali])), with_labels=True)
nx.draw_networkx_edge_labels(G,pos = nx.circular_layout(G),with_labels=True)
nx.draw_networkx_nodes(G,pos=nx.circular_layout(G),nodelist=scenario_num[finali][0:3] , node_shape='d', node_color='b')
nx.draw_networkx_nodes(G,pos=nx.circular_layout(G),nodelist=scenario_num[finali][3:6] , node_shape='8', node_color='g')

#nx.draw(G,nodelist=list(set(G.nodes())-set(scenario_num[finali])),pos=nx.spring_layout(G))
#nx.draw_networkx_nodes(G,pos=nx.spring_layout(G),nodelist=a[all_distances.index(min(all_distances))], node_color='b')
#nx.draw_networkx_nodes(G,pos=nx.spring_layout(G),nodelist=a[no_broke.index(min(no_broke))]          , node_shape='y')

plt.show()

# List test
#a=[0,1,2,3,4,5]
#print a[0:2]
#print a[1:3]






