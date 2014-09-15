import numpy as np
import matplotlib.pyplot as plt
import random


x=range(0,10)
random.shuffle(x)
print x

y=range(0,10)
random.shuffle(y)
print y

m=(y[2]-y[1])/(x[2]-x[1])
c=y[2]-m*x[2]

y=m*13+c

print "slope of line:",m

print "intercept of line:",c

print "value of y:",y

