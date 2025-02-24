## Experiment 3: Multiple Linear Regression in Python & R

### Aim
To understand and implement Multiple Linear Regression using Python and R.

### Theory
Multiple Linear Regression is a statistical method used in predictive modeling that extends the concept of simple linear regression to multiple independent variables. It aims to establish a linear relationship between the dependent variable and multiple predictor variables. In Python, the **Scikit-learn** library is commonly used for implementing multiple linear regression.

### Mathematical Representation
The multiple linear regression equation is represented as follows:

\[ Y = \beta_0 + \beta_1X_1 + \beta_2X_2 + ... + \beta_pX_p + \epsilon \]

Where:
- \( Y \) is the dependent (predicted) variable.
- \( \beta_0 \) is the y-intercept, i.e., the value of \( Y \) when all \( X \) values are 0.
- \( \beta_1, \beta_2, ..., \beta_p \) are the regression coefficients representing the change in \( Y \) relative to a one-unit change in each \( X \) variable.
- \( \epsilon \) is the model’s random error (residual) term.

**Steps in Implementing Multiple Linear Regression in Python:**
1. Import necessary libraries (e.g., NumPy, Pandas, Matplotlib, Scikit-learn).
2. Load and preprocess the dataset.
3. Split the dataset into training and testing sets.
4. Fit the multiple linear regression model using Scikit-learn’s `LinearRegression`.
5. Predict the outcomes for test data.
6. Evaluate the model using metrics like **Mean Squared Error (MSE)** and **R-squared**.
7. Interpret regression coefficients to understand the impact of each independent variable.

### Conclusion
In conclusion, Multiple Linear Regression in Python involves establishing a linear relationship between a dependent variable and multiple independent variables. Using the **Scikit-learn** library, the model is trained, predictions are made, and its performance is evaluated with metrics like **Mean Squared Error** and **R-squared**. Interpretation of coefficients provides insights into variable relationships, and careful consideration of assumptions is crucial for accurate conclusions about the model's reliability and predictive capabilities.
