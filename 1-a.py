import numpy as np
import matplotlib.pyplot as plt
import random


x=range(0,10)
random.shuffle(x)
print x

y=range(0,10)
random.shuffle(y)
print y

plt.scatter(x, y, c='red',label='red',alpha=0.3, edgecolors='none')
plt.legend()
plt.grid(True)

plt.show()


