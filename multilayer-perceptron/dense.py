import numpy as np
from layer import Layer

class Dense(Layer):
	def __init__(self, input_size, output_size, initialiser, seed=None):

		if seed != -1:
			np.random.seed(seed)
		
		if initialiser == "heUniform":
			limit = np.sqrt(6 / input_size)
			self.weights = np.random.uniform(-limit, limit, size=(output_size, input_size))
		else:
			self.weights = np.random.randn(output_size, input_size) #in case randn give too big, might change ltr (row = outputsize, col = inputsize)
		self.bias = np.zeros((output_size, 1))
	
	def forward(self, input):
		self.input = input
		return np.dot(self.weights, input) + self.bias #outputs y
	
	def backward(self, output_gradient, learning_rate):
		#calculate gradient
		weights_gradient = np.dot(output_gradient, self.input.transpose())
		bias_gradient = output_gradient
		input_gradient = np.dot(self.weights.transpose(), output_gradient)

		#update variables using gradient descend
		self.weights -= learning_rate * weights_gradient
		self.bias -= learning_rate * bias_gradient

		return input_gradient #return error gradient of previous layer

	
#variables inside each dense layer
# weights - 2D array of [number of neuron / number of outuput][number of input]
# bias - 1D array of [numer of neuron / number of output]
# input - 1D array of [number of input]