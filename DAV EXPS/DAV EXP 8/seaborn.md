# Box Plot of Age Distribution by Class using Seaborn & Matplotlib

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Load built-in dataset
titanic = sns.load_dataset("titanic")

# Box plot of age distribution by class
plt.figure(figsize=(8,5))
sns.boxplot(x="class", y="age", data=titanic)
plt.title("Age Distribution by Class")
plt.xlabel("Class")
plt.ylabel("Age")
plt.show()
