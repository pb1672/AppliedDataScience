import numpy as np
import matplotlib.pyplot as plt
import random


x=range(0,10)
random.shuffle(x)
print x

y=range(0,10)
random.shuffle(y)
print y

d = np.cov(x,y)

print "covariance of x & y:",d

