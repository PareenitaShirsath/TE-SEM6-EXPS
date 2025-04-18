# Page 1

*Fundamental neural network model* that uses weight updates based on the error to pattern in data,  
limitation led to the development of *multi-layer perceptrons (MLP).*

---

# Experiment No: 9

## Aim
To study and implement the single-layer perceptron learning algorithm which is a fundamental supervised learning algorithm used for binary classification.

## Theory
A perceptron is one of the simplest types of artificial neural network.  
The single-layer perceptron consists of a single neuron that applies a weighted sum of inputs and uses an activation function to make a decision.  
It follows a supervised learning approach.

## Structure of Single Layer Perceptron
1. *Inputs* 👦(x_1, x_2, ..., x_n)👦: Feature values of the dataset  
2. *Weights* 👦(w_1, w_2, ..., w_n)👦: Assigned values that determine the importance of each input  
3. *Summation Function:*

\[
   S = \sum_{i=1}^{n} x_i w_i + b
\]

   Where *b* is the bias term.

## Limitations of the Perceptron
- Only solves linearly separable problems  
- Cannot solve XOR since it is not linearly separable  
- Requires careful tuning of learning rate and convergence

## Conclusion
Thus, we have successfully implemented the single-layer perceptron learning algorithm.
