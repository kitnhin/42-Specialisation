## Overview
This project implements linear regression from scratch to predict car prices based on mileage. The goal is to understand basic machine learning concepts, such as mean squared error and gradient descent, without using machine learning libraries.

## Concepts

### Linear Regression
Linear regression finds the best-fit straight line for a given dataset. The prediction model is:

<p align="center"> Predicted price = θ<sub>0</sub> + θ<sub>1</sub> × mileage </p>

Where:
- θ<sub>0</sub> is the y-intercept
- θ<sub>1</sub> is the gradient of the slope

This is equivalent to the standard linear equation y = mx + c.

<p align="center">
<img src="images/simple_linear_regression.png" alt="Linear Regression Example" width="300"/>
</p>

### Loss Function: Mean Squared Error (MSE)
The loss function measures how well the straight line fits the data. MSE represents the average squared difference between the predicted and actual values:

<p align="center">
MSE = (1/m) × Σ (prediction - actual)²
</p>

Where m is the number of data points in the dataset.

Substituting our linear equation:

<p align="center">
MSE = (1/m) × Σ (θ<sub>0</sub> + θ<sub>1</sub> × mileage - actual)²
</p>

The goal is to find the values of θ<sub>0</sub> and θ<sub>1</sub> that minimize MSE.

### Visualizing MSE in 3D
<p align="center">
<img src="images/MSE_graph.png" alt="MSE graph" width="300"/>
</p>

The minimum point on this surface represents the optimal values for our parameters.


### Finding the Minimum: Partial Derivatives
To find the minimum point of the MSE surface, we find the partial derivatives with respect to both parameters:

- **∂MSE/∂θ<sub>0</sub>**: The slope of the surface when moving only in the θ<sub>0</sub> direction
- **∂MSE/∂θ<sub>1</sub>**: The slope of the surface when moving only in the θ<sub>1</sub> direction

At the minimum point, both partial derivatives equal zero (the gradient is flat).

The partial derivatives are:

<p align="center">
∂MSE/∂θ<sub>0</sub> = learningRate * (1/m) × Σ (predicted - actual)
</p>

<p align="center">
∂MSE/∂θ<sub>1</sub> = learningRate * (1/m) × Σ (predicted - actual) × mileage
</p>

Where learningRate is a constant thats later used in gradient descent to optimise step distance

### Gradient Descent Algorithm
Gradient descent is an iterative optimization algorithm that finds the θ<sub>0</sub> and θ<sub>1</sub> that gives the minimum of the MSE function:

1. Start with initial parameter values
2. For each iteration, update the parameters:
   - θ<sub>0</sub> = θ<sub>0</sub> - learningRate × (∂MSE/∂θ<sub>0</sub>)
   - θ<sub>1</sub> = θ<sub>1</sub> - learningRate × (∂MSE/∂θ<sub>1</sub>)

**Why this works:**
- When we're on the left of the minimum point, the gradient is negative, so subtracting it moves us right (toward the minimum)
- When we're on the right of the minimum point, the gradient is positive, so subtracting it moves us left (toward the minimum)
- The magnitude of the gradient is larger when we're farther from the minimum, so we take bigger steps when far away and smaller steps as we approach the optimal point


## Results

After training the model using gradient descent, here are the results:

Linear regression results:
<p align="center">
  <img src="images/result_LR.png" alt="Linear regression results Results" width="400"/>
</p>

Mean squared error:
<p align="center">
  <img src="images/result_mse.png" alt="MSE error graph" width="400"/>
</p>