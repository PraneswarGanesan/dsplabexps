import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = X**2 + Y**2  # Simple function

plt.contour(X, Y, Z)
plt.show()
