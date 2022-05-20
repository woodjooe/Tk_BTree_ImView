import copy
l=[[1,3,5,6],[10,5,2,6]]
print(l)
l2=copy.deepcopy(l)
print(l2)
l[1][2]=0
print(l)
print(l2)
