import scipy.stats as s
import numpy as np
import matplotlib.pyplot as plt

##### you can find the dataset here: https://grouplens.org/datasets/movielens/100k/
dataa = np.loadtxt("u.data")
data=dataa[:,][:,2]

plt.title('Rating distribution')
plt.xlabel('rating scale')
plt.ylabel('rating frequency')

#### Weibull Function
def weib(x,n,a):#(x,scale,shape)or (x, eta, beta)
    return (a / n) * (x / n)**(a - 1) * np.exp(-(x / n)**a)

#### Parameter Setting (keep location at zero)
(scale, loc, shape) = s.weibull_min.fit(data, floc=0)
print (scale, shape)

## Plot the total distribution of ratings
x = np.linspace(data.min(), data.max(), 50)
plt.plot(x, weib(x, scale, shape),'r--', linewidth=1)
plt.grid(True)
plt.show()
