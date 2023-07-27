import networkx as nx
import matplotlib.pyplot as plt
import itertools
import random


G=nx.gnp_random_graph(5,0.5)
for (u, v) in G.edges():
    G.edge[u][v]['weight'] = random.randint(0,1000)



a=list(itertools.combinations(nx.nodes(G),3))



#for i in a:
#    distance=0
#    dest_calc()
#    for j in dest_combs:
        
    
print (nx.all_simple_paths(G, source=0, target=3))
print (list(nx.all_simple_paths(G, source=0, target=3)))

print ("***")

all_src_dis_comb=[]
temp=[]
d=0
for j in itertools.product([0,1,2,3,4,5],[6,7]):
    ## j is tuple
    temp.append(list(j))
    d+=1
    if d==2:  ## list all different cases of a source node together (for example # servers placement : d==3)
        all_src_dis_comb.append(list(temp))
        d=0
        temp=[]



print (all_src_dis_comb)
print ("***")
print(list(itertools.product(*all_src_dis_comb)))
print ("***")



nx.draw_circular(G,with_labels=True)
plt.show()




#### distances list print , second try
##w=min(all_distances)
##for i in range(0,len(all_distances)):
##    if(-0.0001<all_distances[i]-w<0.0001):
##        all_distances_min.append([i,all_distances[i]])
##
##
##w=min(no_broke)
##for i in range(0,len(no_broke)):
##    if(-0.0001<no_broke[i]-w<0.0001):
##        no_broke_min.append([i,no_broke[i]])
##print ('**NO BROKE MINs LIST - Len :**',len(no_broke_min),'& all sets',no_broke_min)
##
##
#######################################
##
##nx.draw_circular(G,with_labels=True,nodelist=list(set(G.nodes())-set(a[all_distances.index(min(all_distances))])-set(a[no_broke.index(min(no_broke))])))
##nx.draw_networkx_edge_labels(G,pos = nx.circular_layout(G),with_labels=True,nodelist=list(set(G.nodes())-set(a[all_distances.index(min(all_distances))])-set(a[no_broke.index(min(no_broke))])))
##nx.draw_networkx_nodes(G,pos=nx.circular_layout(G),nodelist=a[all_distances.index(min(all_distances))], node_color='b')
##nx.draw_networkx_nodes(G,pos=nx.circular_layout(G),nodelist=a[no_broke.index(min(no_broke))]          , node_shape='d')
##
##plt.show()


