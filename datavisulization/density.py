import matplotlib.pyplot as plt
import numpy as np

data = np.random.randn(1000)  # Random data
plt.hist(data, bins=30, density=True)  # Histogram as density plot
plt.show()
