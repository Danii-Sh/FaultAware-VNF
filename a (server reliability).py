import networkx as nx
import matplotlib.pyplot as plt
import itertools
import random

#G=nx.fast_gnp_random_graph(10,0.3)
G=nx.gnp_random_graph(10,0.5)
#G=nx.complete_graph(10)  # remove weights and print all_distances & no_broke to test if code works correct
for (u, v) in G.edges():
    G.edge[u][v]['weight'] = random.randint(0,100)

#nx.draw_circular(G,with_labels=True)
#plt.ion()
#plt.show()
#plt.show(block=False)
#plt.draw()

#print(nx.nodes(G))
#for i in nx.nodes(G):
#    print(nx.nodes(G)[i])


##for i in nx.nodes(G):
##    distance=0
##    for j in nx.nodes(G):
##        try: distance+=nx.shortest_path_length(G,source=i,target=j)
##        except: distance+=100
##    print distance
##

#print(nx.shortest_path_length(G,weight='weight'))
#print(nx.get_edge_attributes(G,'weight'))

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
##        print(distance)
##        print(b)
##        t=raw_input('')
    distance+=b
    all_distances.append(distance)
    no_broke.append(b)

print(type(i))
print(type(i[1]))


print('****** Printing all lists and min of lists ******')
#### distances list print : all and no_broke  : not working because of float in binary inherent problem

###print(all_distances)
all_distances_min=[]
##
##print(min(all_distances))
##print(all_distances.index(min(all_distances)))
##print all_distances.count(min(all_distances))
##for i in range(0,all_distances.count(min(all_distances))):
##    all_distances_min.append([min(all_distances),all_distances.index(round(min(all_distances),4),(i-1))])
##print all_distances_min
##
###print(no_broke)
no_broke_min=[]        
##for i in range(0,no_broke.count(min(no_broke))):
##    no_broke_min.append([min(no_broke),no_broke.index(min(no_broke),(i-1))])
##print no_broke_min


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


#print(len(all_distances))
print('')
print(min(all_distances),all_distances.index(min(all_distances)), a[all_distances.index(min(all_distances))])
print(min(no_broke),no_broke.index(min(no_broke)) , a[no_broke.index(min(no_broke))])



#######  some general Tests on python and NetworkX
##print(list(itertools.combinations(nx.nodes(G),3)))
##print ((list(itertools.combinations(nx.nodes(G),3))[10])[1])    #test itertools
##print(len(list(itertools.combinations(nx.nodes(G),3))))    
##print(min(80, 100, 1000))       #test min
##
##x=[(2,4,5),(6,8,7)]  ## test python lists
##print(x[1][0])
##
##
##print(type(G.nodes()))
##print(type(a[all_distances.index(min(all_distances))]))
##print nx.edges(G)
######## end of general tests ############


nx.draw_circular(G,with_labels=True,nodelist=list(set(G.nodes())-set(a[all_distances.index(min(all_distances))])-set(a[no_broke.index(min(no_broke))])))
nx.draw_networkx_edge_labels(G,pos = nx.circular_layout(G),with_labels=True,nodelist=list(set(G.nodes())-set(a[all_distances.index(min(all_distances))])-set(a[no_broke.index(min(no_broke))])))
nx.draw_networkx_nodes(G,pos=nx.circular_layout(G),nodelist=a[all_distances.index(min(all_distances))], node_color='b')
nx.draw_networkx_nodes(G,pos=nx.circular_layout(G),nodelist=a[no_broke.index(min(no_broke))]          , node_shape='d')
                       #nodelist=list(a[all_distances.index(min(all_distances))]))

plt.show()







'''
conclusion :
changing link prob (???)  
changing weight range (wider range means more chance to make paths differ largely so causes less number of minimums and also different results for broke vs no broke )
changing reliabiliy   (more break chance means more difference in broke vs no broke)

'''
