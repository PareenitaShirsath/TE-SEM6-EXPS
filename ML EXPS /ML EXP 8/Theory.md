# Experiment No: 8

*Aim*:  
To Study and Implement McCulloch-Pitts (M-P) Model, which is foundational artificial neuron model used in artificial network.

---

*Theory*:  
The McCulloch-Pitts Model, proposed by Warren & Walter Pitts in 1943, is the simplest computational model of a neuron.  
It is a binary threshold-based neuron that forms the basis of modern AI neural networks.

---

### Structure of the M-P Model:

1. *Input* (x₁, x₂, ..., xₙ)  
   Represented as binary values (0 or 1).

2. *Weights* (w₁, w₂, ..., wₙ)  
   Each input has an associated weight that is represented.

3. *Summation Function*:  
\[
   S = \sum_{i=1}^{n} x_i w_i
\]

4. *Threshold*:  
   A predefined value that determines neuron activation.  

   *Mathematically*:
\[
   y = 
   \begin{cases} 
   1, & \text{if } S > \theta \\
   0, & \text{if } S \leq \theta
   \end{cases}
\]

---

### Limitations of McCulloch-Pitts Model:

- Only works with binary inputs (0 and 1)  
- Can only represent linear functions, making it incapable of solving complex problems like XOR  
- Does not support learning (weights and threshold are fixed)

---

*Conclusion*:  
The McCulloch-Pitts Model is the foundation of modern artificial neural networks.  
It demonstrates how a neural unit can process input using weighted summation & a threshold activation function.
