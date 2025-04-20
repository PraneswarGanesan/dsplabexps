import pandas as pd
import matplotlib.pyplot as plt

# Messy employee data
data = {
    'name': ['Asha', 'Bob', 'Cathy', 'Dan', 'Ella', 'Farhan', 'Gita', 'Hari'],
    'department': ['HR', 'hr', 'Sales', 'SALES', 'marketing', 'Marketing', 'Hr', 'sales']
}

df = pd.DataFrame(data)
# Normalize department values
df['department'] = df['department'].str.lower().str.strip()

# Capitalize for clean plot labels
df['department'] = df['department'].replace({
    'hr': 'HR',
    'sales': 'Sales',
    'marketing': 'Marketing'
})

# Count the occurrences of each department
dept_counts = df['department'].value_counts()
# Plot the department distribution
plt.bar(dept_counts.index, dept_counts.values, color=['#4D55CC', '#7A73D1', '#B5A8D5'])
plt.title("Employee Count by Department")
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.show()











--------with machine learining
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Example data
data = {
    'hours': [1, 2, 3, 4, 5],
    'marks': [35, 45, 50, 65, 70]
}

df = pd.DataFrame(data)

# X should be 2D, y should be 1D
X = df[['hours']]  # input (2D)
y = df['marks']    # output (1D)

# Train model
model = LinearRegression()
model.fit(X, y)
# Predict values
predicted = model.predict(X)

# Plot
plt.scatter(df['hours'], df['marks'], color='blue', label='Actual')
plt.plot(df['hours'], predicted, color='red', label='Regression Line')
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.legend()
plt.show()
