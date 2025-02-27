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
y = (X['Spending Score (1-100)'] > X['Spending Score (1-100)'].median()).astype(int)  # Binary target

# Standardizing the features
X = (X - X.mean()) / X.std()

# Single Layer Perceptron Implementation
def perceptron_train(X, y, learning_rate=0.01, epochs=100):
    weights = np.zeros(X.shape[1])
    bias = 0

    for _ in range(epochs):
        for i in range(len(y)):
            prediction = np.dot(X.iloc[i], weights) + bias
            y_pred = 1 if prediction >= 0 else 0
            error = y[i] - y_pred
            weights += learning_rate * error * X.iloc[i]
            bias += learning_rate * error

    return weights, bias

# Training perceptron
weights, bias = perceptron_train(X, y)

# Prediction
def perceptron_predict(X, weights, bias):
    return np.where(np.dot(X, weights) + bias >= 0, 1, 0)

y_pred = perceptron_predict(X, weights, bias)

# Display output
print("Predicted Binary Outputs:", y_pred)

# Visualization
plt.figure(figsize=(8,6))
plt.scatter(X['Annual Income (k$)'], X['Spending Score (1-100)'], c=y_pred, cmap='coolwarm')
plt.title("Customer Segmentation using Single Layer Perceptron")
plt.xlabel("Annual Income (standardized)")
plt.ylabel("Spending Score (standardized)")
plt.show()
