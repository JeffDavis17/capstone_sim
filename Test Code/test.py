import numpy as np
from matplotlib import pyplot as plt
from random import seed
from random import randint


# Test Test_R  30:
'''
Comparing gathered intensity values of buildings of interests during the morning, 
afternoon and evening to test for variability. This will be done by comparing the mean, 
standard deviation and residual analysis of the intensity values of individual cells between two times.   
'''
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


