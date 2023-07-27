import networkx as nx
import matplotlib.pyplot as plt
import itertools
import random

import time
start_time = time.time()
print "Timer started"

num_of_nodes=3
num_of_servers=2


G=nx.gnp_random_graph(num_of_nodes,0.7)
for (u, v) in G.edges():
    G.edge[u][v]['weight'] = random.randint(0,1000)


a=list(itertools.combinations(nx.nodes(G),num_of_servers))
for i in a:
    all_src_dest_comb=[]
    temp=[]
    d=0
    for j in itertools.product(list(nx.nodes(G)),i):
        temp.append(list(j))
        d+=1
        if d==num_of_servers:  ## list all different cases of a source node together (for example # servers placement : d==3)
            all_src_dest_comb.append(list(temp))
            d=0
            temp=[]
    b=list(itertools.product(*all_src_dest_comb))
    print ("$$$ Server Place comb $$                              ", i)
    for j in b:
        print ("@@ source dest comb",j)
        all_path_comb=[]
        for k in j:
#            print (k)
## first tried route : if/else (tried to add [0,0] path , but not needed , as it is the only simple path) so:
## second tried route : ignore the case when src-dest are the same , and only consider different ones
#            if(k[0]==k[1]):
#                v=1
#                all_path_comb.append([])
#                all_path_comb[0].append(k[0])
#                all_path_comb[0].append(k[1])
#            else:
#                all_path_comb.append(list(nx.all_simple_paths(G, source=k[0], target=k[1]))) 

            if (k[0]!=k[1]):
                all_path_comb.append(list(nx.all_simple_paths(G, source=k[0], target=k[1])))
        print ("! all paths",list(all_path_comb))
        c=list(itertools.product(*(all_path_comb)))
        for k in c:
            print ("% each Path comb",k)
            v=1
            
#    print(list(b))



#for i in a:
#    distance=0
#    dest_calc()
#    for j in dest_combs:



        
    
#print (nx.all_simple_paths(G, source=0, target=3))
#print (list(nx.all_simple_paths(G, source=0, target=3)))

print ("***")

#print (all_src_dest_comb)
print ("***")
#print(list(itertools.product(*all_src_dest_comb)))
print ("***")




print("%s seconds" % (time.time() - start_time))




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


