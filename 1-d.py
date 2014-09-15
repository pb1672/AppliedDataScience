import numpy as np
import matplotlib.pyplot as plt
import random


x=range(0,10)
random.shuffle(x)
print x

y=range(0,10)
random.shuffle(y)
print y

print "standard deviation of x:",np.std(x)
print "standard deviation of y:",np.std(y)

