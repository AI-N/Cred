import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import math
import csv
from pandas import DataFrame

##### you can find the dataset here: https://grouplens.org/datasets/movielens/100k/
data=np.genfromtxt('u.data',delimiter='\t')

uID=data[:,][:,0]     # first column
mID=data[:,][:,1]     # second column
rating=data[:,][:,2]  #third column
time=data[:,][:,3]

### number of rows(users), columns(movies) and variety of ratings given by users
MIN_uID=int(min(uID))
MAX_uID=int(max(uID))

MIN_mID=int(min(mID))
MAX_mID=int(max(mID))

MIN_rating=min(rating)
MAX_rating=max(rating)

print ('Num of Users: ',MIN_uID,' to ',MAX_uID, '\nNum of Movies: ',MIN_mID,' to ',MAX_mID,'\nRange of ratings given by users: ',MIN_rating, ' to ',MAX_rating)
rating_Variety=np.unique(rating)
print ('Variety of ratings given by users are: ', rating_Variety)

##### Raing Matrix
Init_Mat=pd.DataFrame(data=data,index=range(len(data)),columns=['uID','mID','rating','time'])  ##making a dataFrame with columns:['uID','mID','rating']
Init_Mat=Init_Mat.sort_values(by=['uID','mID'])
Init_Matrix=np.array(Init_Mat) #making array
print ('\nA head of array of initial matrix with columns:[uID,mID,rating]:\n',Init_Mat.head())
print('\n---for example:---\nInit_Matrix[1][2] is: ',Init_Matrix[1][2],'\n   means:the data in row 2 column 3')  #data in row 2 column 3
Rating_Matrix=np.zeros((len(np.unique(uID)),len(np.unique(mID))),float)

i=iter(Init_Matrix)
for j in range(len(Init_Matrix)):
    n=next(i)
    x=int(n[0])
    y=int(n[1])
    Rating_Matrix[x-1][y-1]=n[2]
       
print('\n*** the Rating_Matrix is:***\n',Rating_Matrix)

center=3.97  #the center of total Weibull distribution for all real ratings
Cr=[]  #credibility values for all users
for i in range(len(Rating_Matrix)):
    print(i)
    a=Rating_Matrix[i]
    x=a[np.nonzero(a)]
    x_bar=np.mean(x)
    x_perim=[]
    if x_bar<=center:
        for k in range(len(x)):
            x_perim.append(5-((5-x[k])*(x_bar/center)))
        AE=np.mean(abs(x-x_perim))
        AE_min=min(abs(x-x_perim))
        Cr.append(np.exp(-(AE-AE_min)))
    else:
        for k in range(len(x)):
            x_perim.append(x[k]*(x_bar/center))
        AE=np.mean(abs(x-x_perim))
        AE_min=min(x-x_perim)
        Cr.append(np.exp(-(AE-AE_min)))
    
#print(Cr)
  
    
