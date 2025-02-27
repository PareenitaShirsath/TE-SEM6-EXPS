from google.colab import files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Upload the dataset
uploaded = files.upload()

# Load the dataset
df = pd.read_csv("Mall_Customers.csv")

# Display first few rows
display(df.head())

# Selecting relevant features
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# McCulloch-Pitts Model Implementation
def mcp_neuron(inputs, weights, threshold):
    weighted_sum = np.dot(inputs, weights)
    return 1 if weighted_sum >= threshold else 0

# Define binary input dataset
X_binary = np.where(X > X.median(), 1, 0)
weights = np.array([1, 1])  # Example weights
threshold = 1  # Example threshold
# Applying McCulloch-Pitts neuron
y_pred = np.array([mcp_neuron(row, weights, threshold) for row in X_binary])
# Removed .values as it's not needed for NumPy arrays
# Display output
print("Predicted Binary Outputs:", y_pred)

# Visualization
plt.figure(figsize=(8,6))
plt.scatter(X['Annual Income (k$)'], X['Spending Score (1-100)'], c=y_pred, cmap='coolwarm')
plt.title("Customer Segmentation using McCulloch-Pitts Model")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.show()
