# Experiment No. 7

*Aim:*  
To implement Expectation Maximization algorithms for a given sample data.

*Theory:*  
The Expectation Maximization (EM) algorithm is an iterative method used in unsupervised ML to estimate unknown parameters in statistical models. It helps to find the best values for unknown parameters, especially when some data is missing or hidden.  

It works in 2 steps:  

*E-step*  
Estimates missing or hidden values using current parameter estimates.  

*M-step*  
Updates model parameters to maximize the likelihood based on the estimated values from the E-step.  

This process repeats until the model reaches a stable solution, improving accuracy with each iteration.  

EM is widely used in clustering & handling missing data.  

---

## Algorithm:

1. *Initialization:*  
   Start with initial parameters, assuming a model for the data.

2. *E-step (Expectation):*  
   Estimate missing data & calculate the posterior probability of latent variables based on current parameters.  
   Compute the log-likelihood of observed data.

3. *M-step (Maximization):*  
   Update model parameters by maximizing the log-likelihood from the E-step, solving an optimization problem.  

4. *Convergence:*  
   Check if parameters are stable. If not, repeat steps 2 & 3 until convergence.

---

*Conclusion:*  
Thus, we have studied & successfully implemented Expectation Maximization algorithm for customer segmentation.
