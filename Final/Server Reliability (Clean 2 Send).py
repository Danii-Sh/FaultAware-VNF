import networkx as nx
import matplotlib.pyplot as plt
import itertools
import random


G=nx.gnp_random_graph(10,0.5)

print ((G.edges))

for (u) in G.edges():
    print (u)
    G.edges[u]['weight'] = random.randint(0,1000)



p=0.05   #server_broke_prob
all_distances=[]
no_broke=[]
a=list(itertools.combinations(nx.nodes(G),3))
for i in a:
    distance=0
    b=0
    for j in nx.nodes(G):
        distance+= p*p*(1-p)*(nx.shortest_path_length(G,source=i[0],target=j,weight='weight'))  #server 1 and 2 broke
        distance+= p*p*(1-p)*(nx.shortest_path_length(G,source=i[1],target=j,weight='weight'))  #server 0 and 2 broke
        distance+= p*p*(1-p)*(nx.shortest_path_length(G,source=i[2],target=j,weight='weight'))  #server 0 and 1 broke
        distance+= p*(1-p)*(1-p)*(min((nx.shortest_path_length(G,source=i[0],target=j,weight='weight')),(nx.shortest_path_length(G,source=i[1],target=j,weight='weight'))))  #server 2 broke
        distance+= p*(1-p)*(1-p)*(min((nx.shortest_path_length(G,source=i[0],target=j,weight='weight')),(nx.shortest_path_length(G,source=i[2],target=j,weight='weight'))))  #server 1 broke
        distance+= p*(1-p)*(1-p)*(min((nx.shortest_path_length(G,source=i[1],target=j,weight='weight')),(nx.shortest_path_length(G,source=i[2],target=j,weight='weight'))))  #server 0 broke
        b+= (1-p)*(1-p)*(1-p)*(min((nx.shortest_path_length(G,source=i[0],target=j,weight='weight')),(nx.shortest_path_length(G,source=i[1],target=j,weight='weight')),\
                                      (nx.shortest_path_length(G,source=i[2],target=j,weight='weight'))))  #no servers broke

    distance+=b
    all_distances.append(distance)
    no_broke.append(b)


print('****** Printing all lists and min of lists ******')

all_distances_min=[]
no_broke_min=[]        


#### distances list print , second try
w=min(all_distances)
for i in range(0,len(all_distances)):
    if(-0.0001<all_distances[i]-w<0.0001):
        all_distances_min.append([i,all_distances[i]])
print ('**ALL DISTANCES MINs LIST - Len :**',len(all_distances_min),'& all sets',all_distances_min)
print('')
w=min(no_broke)
for i in range(0,len(no_broke)):
    if(-0.0001<no_broke[i]-w<0.0001):
        no_broke_min.append([i,no_broke[i]])
print ('**NO BROKE MINs LIST - Len :**',len(no_broke_min),'& all sets',no_broke_min)


#####################################
print('')
print(min(all_distances),all_distances.index(min(all_distances)), a[all_distances.index(min(all_distances))])
print(min(no_broke),no_broke.index(min(no_broke)) , a[no_broke.index(min(no_broke))])


## difference between draw and draw_networkx : the second oe accepts arguments
# 
nx.draw_networkx(G,pos=nx.circular_layout(G),with_labels=True,nodelist=list(set(G.nodes())-set(a[all_distances.index(min(all_distances))])-set(a[no_broke.index(min(no_broke))])))

# ,with_labels=True,nodelist=list(set(G.nodes())-set(a[all_distances.index(min(all_distances))])-set(a[no_broke.index(min(no_broke))]))
nx.draw_networkx_edge_labels(G,pos = nx.circular_layout(G))


nx.draw_networkx_nodes(G,pos=nx.circular_layout(G),nodelist=a[all_distances.index(min(all_distances))], node_color='b')


nx.draw_networkx_nodes(G,pos=nx.circular_layout(G),nodelist=a[no_broke.index(min(no_broke))]          , node_shape='d')

plt.show()




'''
conclusion :
changing link prob (???)  
changing weight range (wider range means more chance to make paths differ largely so causes less number of minimums and also different results for broke vs no broke )
changing reliabiliy   (more break chance means more difference in broke vs no broke)

'''
