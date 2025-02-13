import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
    'Sales': [1200, 1400, 1500, 1550, 1700, 1600, 1750, 1800, 1850, 1900, 2000, 2100]
}

df = pd.DataFrame(data)

x = np.arange(len(df['Month']))
y = np.array(df['Sales'])

slope, intercept, r_value, p_value, std_err = linregress(x, y)

plt.figure(figsize=(10, 6))
plt.scatter(df['Month'], df['Sales'], color='blue', label='Actual Sales', s=100)  
plt.plot(df['Month'], slope * x + intercept, color='red', linestyle='--', label='Trend Line')

plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Monthly Sales Data with More Data Points")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()

print(f"Sales Trend: y = {slope:.2f}x + {intercept:.2f}")
