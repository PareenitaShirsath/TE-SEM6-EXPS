import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression  # Importing LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import numpy as np

# Load data
data = pd.read_csv("temperatures.csv")

# Check if the data is loaded correctly and inspect the column names
print("Data loaded successfully. Columns:", data.columns)

# Ensure the column "YEAR" exists in the dataframe
if "YEAR" in data.columns:
    x = data["YEAR"].values  # No reshape here, just the raw values
else:
    raise ValueError("Column 'YEAR' not found in the CSV file")

y = data["ANNUAL"]

# Convert 'ANNUAL' to binary values (e.g., classify temperatures above a certain threshold)
threshold = y.mean()  # Using the mean as a threshold for classification
y_binary = (y > threshold).astype(int)  # Convert to 1 if above threshold, else 0

# Split the data into training and test sets
x_train, x_test, y_train, y_test = train_test_split(x.reshape(-1, 1), y_binary, test_size=0.2, random_state=0)

# Create the Logistic Regression model and fit it to the training data
model = LogisticRegression()
model.fit(x_train, y_train)

# Make predictions on the test set
y_pred = model.predict(x_test)

# Print accuracy and confusion matrix
print("Accuracy of Logistic Regression model:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))

# Plotting the decision boundary and data points
plt.figure(figsize=(10, 6))  # Optional: Specify figure size
plt.title("Logistic Regression: Temperature Classification")
plt.xlabel("Year")
plt.ylabel("Temperature (Binary Classification)")

# Scatter plot for the original data
plt.scatter(x, y_binary, color='blue', label='Full Data', alpha=0.5)

# Plot the logistic regression curve
x_range = np.linspace(x.min(), x.max(), 100).reshape(-1, 1)
y_range = model.predict_proba(x_range)[:, 1]  # Get probabilities for the positive class
plt.plot(x_range, y_range, color='green', label='Logistic Regression Curve')

# Show the legend to distinguish the points
plt.legend()

# Display the plot
plt.show()

