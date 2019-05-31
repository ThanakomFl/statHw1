import random
import numpy as np 
result=[]
lower=3
upper=6
for x in range(1000000):
  temp=random.uniform(lower,upper)
  result.append(temp**2)
print(lower*np.mean(result))