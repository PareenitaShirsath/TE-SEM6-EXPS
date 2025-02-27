## AIM

To implement the Logistic Regression algorithm for a given dataset and analyze its performance.

## THEORY

Logistic Regression is a classification algorithm used to predict categorical outcomes. Unlike Linear Regression, which deals with continuous values, Logistic Regression predicts the probability of a sample belonging to a particular class. The logistic function (sigmoid function) is given by:

\[ P(y=1|X) = \frac{1}{1 + e^{-(b_0 + b_1x_1 + ... + b_nx_n)}} \]

Where:
- \( P(y=1|X) \) is the probability of the class label being 1,
- \( b_0, b_1, ..., b_n \) are the coefficients of the model,
- The function maps any real number to a value between 0 and 1.

Logistic Regression is widely used for binary classification tasks such as spam detection, medical diagnosis, and credit scoring.
# Logistic Regression

## Theory

Logistic Regression is a classification algorithm used for binary classification problems. It predicts the probability of an instance belonging to a particular class using the **sigmoid function**, which outputs values between 0 and 1. The decision boundary is defined using:

\[
P(y=1|X) = \frac{1}{1 + e^{-(b_0 + b_1x_1 + ... + b_nx_n)}}
\]

where \( b_0, b_1, ..., b_n \) are the model parameters. If the predicted probability is greater than 0.5, the instance is classified as **1**, otherwise, it is classified as **0**.

### Applications:
- Spam detection
- Disease diagnosis
- Customer churn prediction

## CONCLUSION

Logistic Regression is an essential algorithm for classification tasks. It is simple, interpretable, and effective for linearly separable data. However, it may struggle with complex relationships, requiring feature engineering or advanced models for better performance.

---

