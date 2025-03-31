# Line Plot of `flights` Dataset using Matplotlib & Seaborn

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Load built-in dataset
data = sns.load_dataset("flights")

# Line plot
plt.figure(figsize=(8,5))
plt.plot(data["year"], data["passengers"], marker='o', linestyle='-')
plt.title("Number of Passengers Over Years")
plt.xlabel("Year")
plt.ylabel("Passengers")
plt.grid(True)
plt.show()
