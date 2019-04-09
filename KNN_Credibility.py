
import numpy as np
import math
import pandas as pd
from pandas import DataFrame
import heapq
from math import sqrt

header = ['user_id', 'item_id', 'rating','time']
df = pd.read_csv('u.data', sep='\t', names=header)
n_users = df.user_id.unique().shape[0]
n_items = df.item_id.unique().shape[0]
print('Number of users = ' + str(n_users) + ' | Number of movies = ' + str(n_items))

Rating_Matrix = np.zeros((n_users, n_items))
for line in df.itertuples():
    Rating_Matrix[line[1]-1, line[2]-1] = line[3]


################    
#Load Sim which is the similarity matrix
#Load Cr which is calculated through CredibilityValues.py


##KNN without the use of Credibility
n_neighbors=5
indices=np.zeros((n_users,n_neighbors))  #user neighbors' indices
KNN_Sim=np.zeros((n_users,n_neighbors))  #user neighbors' similarity values


for i in range(n_users):
    indices[i]=(heapq.nlargest(n_neighbors, range(len(Sim[i])), key=Sim[i].__getitem__)) #index
    KNN_Sim[i]=(heapq.nlargest(n_neighbors, Sim[i]))   #value
print('\nKNN_indices where num_of_neighbors is: ',n_neighbors,'\n',indices)
print('\nKNN_Sim:\n',KNN_Sim)


##KNN with the use of Credibility
n_neighbors=5

Sim_Cr=np.zeros((n_users,n_items))

for i in range (n_users):
    for j in range(n_items):
        Sim_Cr[i][j]=Sim[i][j]*Cr[[j]


indices_Cr=np.zeros((n_users,n_neighbors))  #user neighbors' indices
KNN_Sim_Cr=np.zeros((n_users,n_neighbors))  #user neighbors' similarity values


for i in range(n_users):
    indices_Cr[i]=(heapq.nlargest(n_neighbors, range(len(Sim_Cr[i])), key=Sim_Cr[i].__getitem__)) #index
    KNN_Sim_Cr[i]=(heapq.nlargest(n_neighbors, Sim_Cr[i]))   #value
print('\nKNN_indices with the use of Credibility where num_of_neighbors is: ',n_neighbors,'\n',indices_Cr)
print('\nKNN_Sim with the use of Credibility:\n',KNN_Sim_Cr)
