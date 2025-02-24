## Experiment 2: Simple Linear Regression in Python

### Aim
To understand and implement Simple Linear Regression using Python.

### Theory
Simple Linear Regression is a statistical method that models the relationship between a dependent variable (Y) and a single independent variable (X) using a linear equation:

\[ Y = b_0 + b_1X + \epsilon \]

Where:
- \( Y \) is the dependent variable (target).
- \( X \) is the independent variable (predictor).
- \( b_0 \) is the intercept.
- \( b_1 \) is the slope of the line (coefficient).
- \( \epsilon \) is the error term.

The goal of Simple Linear Regression is to find the best-fit line that minimizes the sum of squared residuals (differences between actual and predicted values). This is often achieved using the **Ordinary Least Squares (OLS)** method.

**Steps in Implementing Simple Linear Regression in Python:**
1. Import necessary libraries (e.g., NumPy, Pandas, Matplotlib, Scikit-learn).
2. Load and preprocess the dataset.
3. Split the dataset into training and testing sets.
4. Fit the regression model using Scikit-learn's `LinearRegression`.
5. Predict the outcomes for test data.
6. Evaluate the model using metrics like Mean Squared Error (MSE) and R-squared.
7. Visualize the regression line.

### Conclusion
Simple Linear Regression is a fundamental technique in predictive modeling, useful for understanding relationships between variables. Implementing it in Python using Scikit-learn allows efficient data modeling, prediction, and analysis. Mastery of this technique is essential for developing more advanced machine learning models.

