import networkx as nx
import matplotlib.pyplot as plt
import itertools
import random


#G=nx.fast_gnp_random_graph(10,0.3)
G=nx.Graph()

G.add_path([0,1,2])
G.add_path([2,3])
G.add_path([1,3])
G.add_path([0,2])
G.add_path([0,4])

for (u, v) in G.edges():
    G.edge[u][v]['weight'] = random.randint(0,5)
    G.edge[u][v]['Load_Weight'] = 0
    print (u,v)

print('*****Edges*****')

print (G.edge)

print('*****Weight Sample*****')

print(type(G.edge[u][v]['weight']))
print(G.edge[u][v]['weight'])

print('*****All Paths*****')
print(nx.shortest_path_length(G,weight='weight'))

print('*****Trying Algorithm*****')
#first try ?? good notes, trying to edit and improve
##for j in G.nodes():  # yek server ra dar J gharar midahim
##    for i in G.nodes():  # ta nodehaye i
##        if(i!=j):     # be joz az khodash be khodash
##            for path in nx.all_simple_paths(G, source=j, target=i):  # hameye msariha ra miyabim
##                print(path)
##                for x in range(1 , len(path)):
##                    print(len(path))
##                    G.edge[path[x-1]][path[x]]['Load_Weight'] += 1   # va be tak take link in masirha yek vazn ezafe mikonim

###attention to python 'for' structure
##server_no=2
##for i in list(itertools.combinations(G.nodes(),server_no)):
##    print i
##    for x in range(0,server_no):
##        print i[x]
##################################################print('88888')
##################################################print type(nx.all_simple_paths(G, source=1, target=2))
##################################################for i in nx.all_simple_paths(G, source=1, target=2):
##################################################    print i
##################################################print list(nx.all_simple_paths(G, source=1, target=2))
##################################################print('88888')
all_combinations_servers_nodes_paths=[] # [combination][server no][target node][path no]
server_no=2
comb_no=-1
for i in list(itertools.combinations(G.nodes(),server_no)):
    comb_no+=1
    all_combinations_servers_nodes_paths.append([])
    for k in range (0,server_no):
        all_combinations_servers_nodes_paths[comb_no].append([])
        l=0
        for j in G.nodes():
            if j != k:  #traffic is generated between 2 servers                       #if j not in i: traffic is not generated between 2 servers
                #all_combinations_servers_nodes_paths[no][k][j]= nx.all_simple_paths(G, source=i[k], target=j)
                #print(all_combinations_servers_nodes_paths)
                all_combinations_servers_nodes_paths[comb_no][k].append([])
                #print G.nodes()
                #print j
                all_combinations_servers_nodes_paths[comb_no][k][l].append(list(nx.all_simple_paths(G, source=i[k], target=j)))
                l+=1
#print all_combinations_servers_nodes_paths



##### Multi-Dimensional List filled with every server_combination , server number , target node number , path
##### ....[0][0][0][0] = [[0, 1], [0, 2, 1], [0, 2, 3, 1]]
##### ....[0][0][0][0][0] = [0, 1]                
                


##for i in range(0,len (all_combinations_servers_nodes_paths)):
##    for k in range(0,len (all_combinations_servers_nodes_paths[i])):
##        for l in range(0, all_combinations_servers_nodes_paths[i][k]):
##            hameye nodha
##            for m in range(0,all_combinations_servers_nodes_paths[i][k][l]):
##                +1 kardanee hameye link ha
##                e^weight kardane hame linkha
##                jam kardane hameye e^weight ha
##                append kardane javabha be ye liste dige

print (len(all_combinations_servers_nodes_paths),'XOXOXOX')    
print (len(all_combinations_servers_nodes_paths[0]),'XOXOXOX')

for 


for i in range(0,len (all_combinations_servers_nodes_paths)):
    for () #make a vector of actions

    
    for p in Path scenario no: # correct indent : apply previous vector
        for l in range(0, len(all_combinations_servers_nodes_paths[i])): # all servers 
            for m in range(0,all_combinations_servers_nodes_paths[i][k][l]): # all target nodes
                +1 kardanee hameye link ha   #implement and use path scenario no
                e^weight kardane hame linkha
                jam kardane hameye e^weight ha
                append kardane javabha be ye liste dige

nx.draw_networkx(G,pos = nx.circular_layout(G),with_labels=True)
nx.draw_networkx_edge_labels(G,pos = nx.circular_layout(G))
plt.show()

