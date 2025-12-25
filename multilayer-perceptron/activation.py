import numpy as np
import math
from layer import Layer

class Activation(Layer):
	def __init__(self, activation_ft):
		super().__init__()
		self.activation_ft = activation_ft
	
	def forward(self, input):
		self.input = input
		self.output = 1

		if self.activation_ft == "sigmoid":
			self.output = self.sigmoid(input)
		elif self.activation_ft == "softmax":
			self.output = self.softmax(input)
		
		return self.output
	
	def backward(self, output_gradient, learning_rate):
		input_error = 1
		if self.activation_ft == "sigmoid":
			input_error = np.multiply(output_gradient, self.sigmoid_prime(self.input))
		elif self.activation_ft == "softmax":
			input_error = output_gradient
		
		return input_error

	
	#activation functions
	def sigmoid(self, input):
		return 1 / (1 + np.exp(-input))

	def sigmoid_prime(self, input):
		return np.exp(-input) / (1 + np.exp(-input))**2
	
	def softmax(self, input): #special activation function that make the output dependent on each other (can read up on this ltr)
		exp_values = np.exp(input - np.max(input))
		return exp_values / np.sum(exp_values)
	