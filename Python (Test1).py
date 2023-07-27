import itertools

a=[1,2,3]
b=(1,2,3)

print(type(a))
print(type(b))

c=set(a)
print(type(c))

print(a)
print(b)
print(c)


print('*****Multi-Dimensional List Test 1*****')
a=[[],[]]
b=[[]]     # @this equals:
#a[0][0]=[0,2]
#b.append([])  # @this
print a
print b
(b[0]).append(2)
print type(b[0])
(b[0]).append(3)
b.append([4])
print b

print('*****Multi-Dimensional List Test 2*****')

i=[]

i.append([])

i[0].append([])

i.append([])
i[1].append([])

print i



print('*****List Min *****')

o=[1,2,3]
o.append([4,5])
print o

j=[5,4,3,2,1,55,7,8,1]       ### Next 5 lines : working
j_min=[]        
for i in range(0,j.count(min(j))):
    j_min.append([min(j),j.index(min(j),(i-1))])
print j_min


print('*****List Indexing Test*****')
t=[[1,2],[3,4]]
print t
b=[1,0]
print t[1][0]
#print t[b]


print('*****Combination*****')
print(list(itertools.combinations([0,1,2,3],3)))
o=list(itertools.combinations([0,1,2,3],3))
print o[1][2]

print('*****Product*****')
print(list(itertools.product([0,1],[2,3],[4,5])))
o=list(itertools.product([0,1],[2,3],[4,5]))
print o[1][2]
print('*****')
print(list(itertools.product([[[0,1],[2,3]],[[4,5]]])))

print('*****Permutation*****')
print(list(itertools.permutations([0,1,2,3],3)))





# List test
a=[0,1,2,3,4,5]
print a[0:2]
print a[1:3]





