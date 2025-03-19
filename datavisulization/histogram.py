import numpy as np
import matplotlib.pyplot as plt

ages = np.random.normal(20,7.5,1000)
# plt.hist(ages, bins=20)
# plt.hist(ages,bins=[ages.min(),18,21,ages.max()])
# cumulative distribution
plt.hist(ages,bins=20,cumulative=True)
# plt.show()
