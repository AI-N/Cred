
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

##### you can find the dataset here: https://grouplens.org/datasets/movielens/100k/
header = ['user_id', 'item_id', 'rating','time']
df = pd.read_csv('u.data', sep='\t', names=header)
n_users = df.user_id.unique().shape[0]
n_items = df.item_id.unique().shape[0]
print('Number of users = ' + str(n_users) + ' | Number of movies = ' + str(n_items))

Rating_Matrix = np.zeros((n_users, n_items))
for line in df.itertuples():
    Rating_Matrix[line[1]-1, line[2]-1] = line[3]



##### Plot first 30 Users' rating behavior
x=[1,2,3,4,5]
yy=[]
fig=plt.figure()
for j in range(30):
    yy=[]
    for i in range(len(x)):
        h=(Rating_Matrix[j]==x[i]).sum()
        yy.append(h)
        #print(x[i],' : ',h)
    y=np.array(yy)
    plt.subplot(5,6,int(j+1))
    plt.bar(x,y,label='U%1.3s' % str(j+1))
    plt.xlabel('rating scale', fontsize=8)
    plt.ylabel('rating frequency',fontsize=8)
    plt.legend(loc='upper left')
    plt.grid(True)
    plt.suptitle('Rating frequency', fontsize=16)
plt.show()
