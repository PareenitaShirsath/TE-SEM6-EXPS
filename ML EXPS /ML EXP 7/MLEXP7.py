from google.colab import files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.mixture import GaussianMixture

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

# Applying Expectation-Maximization using Gaussian Mixture Model
gmm = GaussianMixture(n_components=2, random_state=42)
gmm.fit(X_scaled)
y_pred = gmm.predict(X_scaled)

# Splitting data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_pred, test_size=0.2, random_state=42)

# Evaluation
accuracy = np.mean(gmm.predict(X_test) == y_test)
print("Accuracy:", accuracy)

# Visualization
plt.figure(figsize=(8,6))
sns.scatterplot(x=X_scaled[:, 0], y=X_scaled[:, 1], hue=y_pred, palette='coolwarm')
plt.title("Customer Segmentation using Expectation-Maximization")
plt.xlabel("Annual Income (scaled)")
plt.ylabel("Spending Score (scaled)")
plt.show()

