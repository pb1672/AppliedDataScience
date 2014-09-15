import numpy as np
import matplotlib.pyplot as plt
import random


x=range(0,10)
random.shuffle(x)
print x

y=range(0,10)
random.shuffle(y)
print y

print "variation of x:",np.var(x)
print "variation of y:",np.var(y)

