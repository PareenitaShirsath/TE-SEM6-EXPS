import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression  # Importing LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Load data
data = pd.read_csv("temperatures.csv")

# Check if the data is loaded correctly and inspect the column names
print("Data loaded successfully. Columns:", data.columns)

# Ensure the column "YEAR" exists in the dataframe
if "YEAR" in data.columns:
    x = data["YEAR"].values.reshape(-1, 1)  # Reshaping for sklearn compatibility
else:
    raise ValueError("Column 'YEAR' not found in the CSV file")

# Ensure the column "ANNUAL" exists in the dataframe
if "ANNUAL" in data.columns:
    y = data["ANNUAL"].values
else:
    raise ValueError("Column 'ANNUAL' not found in the CSV file")

# Split the data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Create the Linear Regression model and fit it to the training data
model = LinearRegression()
model.fit(x_train, y_train)

# Make predictions on the test set
y_pred = model.predict(x_test)

# Print model evaluation metrics
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R² Score:", r2_score(y_test, y_pred))

# Plotting the regression line
plt.figure(figsize=(10, 6))  # Optional: Specify figure size
plt.title("Linear Regression: Year vs Temperature")
plt.xlabel("Year")
plt.ylabel("Annual Temperature")

# Scatter plot for the original data
plt.scatter(x, y, color='blue', label='Actual Data', alpha=0.5)

# Plot the regression line
plt.plot(x, model.predict(x), color='red', linewidth=2, label='Regression Line')

# Show the legend to distinguish the points
plt.legend()

# Display the plot
plt.show()

