from google.colab import files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

# Upload the dataset
uploaded = files.upload()

# Load the dataset
df = pd.read_csv("Mall_Customers.csv")

# Display first few rows
display(df.head())

# Selecting relevant features
X = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Standardizing the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Initializing weights
weights = np.random.rand(X_scaled.shape[1])
bias = np.random.rand()
learning_rate = 0.01

# Hebbian Learning Function
def hebbian_learning(X, y, weights, bias, learning_rate):
    for i in range(len(X)):
        weights += learning_rate * y[i] * X[i]
        bias += learning_rate * y[i]
    return weights, bias

# Creating target variable (Clustering customers into 2 groups for simplicity)
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, random_state=42)
y = kmeans.fit_predict(X_scaled)

# Splitting data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Training using Hebbian Learning
weights, bias = hebbian_learning(X_train, y_train, weights, bias, learning_rate)

# Predictions
y_pred = np.sign(np.dot(X_test, weights) + bias)

# Evaluation
accuracy = np.mean(y_pred == y_test)
print("Accuracy:", accuracy)

# Visualization
plt.figure(figsize=(8,6))
sns.scatterplot(x=X_scaled[:, 0], y=X_scaled[:, 1], hue=y, palette='coolwarm')
plt.title("Customer Segmentation using Hebbian Learning")
plt.xlabel("Annual Income (scaled)")
plt.ylabel("Spending Score (scaled)")
plt.show()

