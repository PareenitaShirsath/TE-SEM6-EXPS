# Implementation of Hebbian Learning for Customer Segmentation

## AIM
To implement Hebbian Learning for customer segmentation based on annual income and spending score, using an unsupervised clustering approach with K-Means and evaluating its effectiveness.

---

## THEORY

### Customer Segmentation – Clustering
Clustering is a technique used to categorize customers into distinct groups based on similar characteristics. In this case, we use **Annual Income** and **Spending Score** as features.

### Feature Scaling
Standardization using **StandardScaler** ensures uniformity in data distribution for better clustering and learning performance.

### K-Means Clustering
An **unsupervised machine learning algorithm** used to classify customers into two groups. It assigns data points to clusters based on **similarity (distance metric).**

### Hebbian Learning Rule
A simple neural learning algorithm that updates weights based on the **correlation between input and output.** It follows the principle:

\[
w_{\text{new}} = w_{\text{old}} + \eta \cdot y \cdot X
\]

where:  
- \( \eta \) is the **learning rate**  
- \( y \) is the **target output**  
- \( X \) is the **input feature**

### Model Evaluation
The accuracy of Hebbian Learning is measured by comparing predicted labels with actual cluster labels.

---

## CONCLUSION
- The implemented **Hebbian Learning algorithm** successfully classifies customers into two segments based on their **spending patterns**.  
- The **accuracy score** indicates the effectiveness of Hebbian Learning in **customer segmentation**.  
- **Visualization** confirms that the clustering results align with distinct customer groups.  
- While Hebbian Learning provides a simple approach, **more sophisticated models like Neural Networks or Supervised Learning Algorithms** may yield better results for complex segmentation tasks.  

