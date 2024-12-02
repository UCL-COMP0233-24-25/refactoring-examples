"""This code produces a tree-like plot."""

from math import sin, cos
from matplotlib import pyplot as plt
branch_size=5
loc=[[1,1,1]]
nodes = 5
plt.plot([0,0],[0,1])
for i in range(nodes):
    add_branch=[]
    for j in range(len(loc)): 
        
        add_branch.append([loc[j][0]+branch_size*sin(loc[j][2]-0.1), loc[j][1]+branch_size*cos(loc[j][2]-0.1), loc[j][2]-0.1])
        add_branch.append([loc[j][0]+branch_size*sin(loc[j][2]+0.1), loc[j][1]+branch_size*cos(loc[j][2]+0.1), loc[j][2]+0.1])
        
        plt.plot([loc[j][0], add_branch[-2][0]],[loc[j][1], add_branch[-2][1]])
        plt.plot([loc[j][0], add_branch[-1][0]],[loc[j][1], add_branch[-1][1]])
    loc=add_branch
    branch_size*=0.6
plt.savefig('tree_s5_d111.png')
