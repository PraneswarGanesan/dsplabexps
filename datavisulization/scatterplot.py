import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Generate random data
x_data = np.random.random(50) * 100
y_data = np.random.random(50) * 100

print(x_data)
print(y_data)

# Perform linear regression
slope, intercept, r_value, p_value, std_err = linregress(x_data, y_data)

# Plot scatter plot
plt.scatter(x_data, y_data, c="red", s=10, marker="*", alpha=0.3)

# Plot regression line
plt.plot(x_data, slope * x_data + intercept, color="red", linestyle="--", label='Simple Linear Regression')

# Labeling the axes
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

# Add grid and legend
plt.grid(True)
plt.legend()
plt.show()
