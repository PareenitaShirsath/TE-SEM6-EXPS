## Aim
To study and implement the Error Backpropagation Training Algorithm which is used for training Multi-layer Perceptrons (MLPs) using gradient descent.

---

## Theory

The Error Propagation Algorithm is a fundamental method for training multi-layer perceptrons (MLPs) in artificial neural networks.  
It minimizes the error by adjusting the weights using gradient descent.  
This method is widely used in deep learning and supervised learning problems.

The Backpropagation consists of two main phases:

### 1. Forward Propagation
- Inputs are passed through the network.
- Each neuron applies the weighted sum and an activation function.
- The network generates an output based on the current weights.

### 2. Backward Propagation
- The error is calculated as the difference between the actual output and the expected target.
- Weights are updated using the gradient descent rule:

$$
W_{ij} = W_{ij} + \eta \cdot \delta_j \cdot x_i
$$

Where:  
- \( \eta \) = learning rate  
- \( \delta_j \) = error term for the neuron  
- \( x_i \) = input to the neuron  

Also, the error function used is:

$$
E = \frac{1}{2} \sum (t - o)^2
$$

Where:  
- \( E \) = error  
- \( t \) = target output  
- \( o \) = obtained output  

---

## Conclusion
Thus, we have successfully implemented the Error Backpropagation Training Algorithm,  
which is used for training multi-layer perceptrons.
