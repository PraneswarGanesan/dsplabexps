import matplotlib.pyplot as plt
import numpy as np

x = np.arange(1, 6)
y = np.array([2, 3, 5, 4, 6])
errors = np.array([0.2, 0.3, 0.1, 0.2, 0.3])

plt.errorbar(x, y, yerr=errors, fmt='o')
plt.show()
