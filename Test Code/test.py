import numpy as np
import matplotlib.pyplot as plt
from random import seed
from random import randint


# Test Test_R  30:
# Range usually between -88 and -55, analyzing 4 cells, with 3 readings: Morning, Noon, Evening
v = []
t_val = np.array([-67,-81,-58,-62]) # "True" intensity values
noise = np.array([5,3,1]) # Expected Noise over the day
for i in range(3):
    val = [randint(t_val[0] - noise[i],t_val[0] + noise[i]),randint(t_val[1] - noise[i],t_val[1] + noise[i]),randint(t_val[2] - noise[i],t_val[2] + noise[i]),randint(t_val[3] - noise[i],t_val[3] + noise[i])]
    v.append(val)
v = np.array(v)


# Analysis
val = np.around(np.array([np.mean(v[:,0]),np.mean(v[:,1]),np.mean(v[:,2]),np.mean(v[:,3])])) # Field Measured Average
s = np.array([np.std(v[:,0]),np.std(v[:,1]),np.std(v[:,2]),np.std(v[:,3])]) # Field Measured Standard Deviation


# Residual Plot
res = np.array(v,dtype=float)
res[:,0] -= val[0] 
res[:,1] -= val[1]
res[:,2] -= val[2]
res[:,3] -= val[3]
print(res)


# BAR CHART 

m = np.array([1,1,1,3])
a = np.array([1,1,1,0])
e = np.array([1,1,1,1])

m = np.mean(m)
a = np.mean(a)
e = np.mean(e)

x = ["morning", "afternoon", "evening"]
plt.figure()
plt.bar(x,[m,a,e])
plt.show()