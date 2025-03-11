
# AIM
**Implementation of the ARIMA model in Python**

# THEORY
ARIMA (AutoRegressive Integrated Moving Average) is a popular time series forecasting model that combines autoregression (AR) and moving average (MA) techniques with differencing to handle non-stationary data.

## Components of ARIMA

### 1. AutoRegressive (AR) Component
ARIMA(p,d,q) includes the AR(p) component, where the value of the time series at a certain point is regressed on its previous values. The parameter 'p' represents the number of lag observations included in the model.

### 2. Integrated (I) Component
ARIMA(p,d,q) also includes the differencing step, represented by 'd', which involves differencing the raw observations (subtracting the previous value from the current value) to make the time series stationary.

### 3. Moving Average (MA) Component
ARIMA(p,d,q) includes the MA(q) component, where the regression error is a linear combination of the error terms from previous time steps. The parameter 'q' represents the size of the moving average window.

# CONCLUSION
We successfully applied the ARIMA model to the provided dataset and evaluated its performance. We first loaded the dataset, split it into training and testing sets, and then fit the ARIMA model to the training data. We visualized the actual vs. predicted sales values for both the training and testing sets to assess the model's performance visually.
```

