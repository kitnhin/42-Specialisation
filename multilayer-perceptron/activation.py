import numpy as np
import math
from layer import Layer
import activation_ft as af

class Activation(Layer):
	def __init__(self, activation_ft):
		super().__init__()
		self.activation_ft = activation_ft
	
	def forward(self, input):
		self.input = input
		self.output = 1

		if self.activation_ft == "sigmoid":
			self.output = af.sigmoid(input)
		elif self.activation_ft == "softmax":
			self.output = af.softmax(input)
		
		return self.output
	
	def backward(self, output_gradient, learning_rate):
		input_error = 1
		if self.activation_ft == "sigmoid":
			input_error = np.multiply(output_gradient, af.sigmoid_prime(self.input))
		elif self.activation_ft == "softmax":
			input_error = output_gradient
		
		return input_error
	