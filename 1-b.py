import numpy as np
import matplotlib.pyplot as plt
import random


x=range(0,10)
random.shuffle(x)
print x

y=range(0,10)
random.shuffle(y)
print y

print "mean of x:",np.mean(x)
print "mean of y:",np.mean(y)

