import argparse
import json
import numpy as np
import statistics as st
import preprocess_data as pd
import matplotlib.pyplot as plot

from dense import Dense
from activation import Activation

def construct_network(data, layers):
	#construct network
	network = []

	#first layer
	input_size = len(data[0]) #number of fields
	output_size = layers[0]
	network.append(Dense(input_size, output_size)) #first input layer
	network.append(Activation("sigmoid"))
	prev_out_size = output_size

	#hidden layers
	for i in range(len(layers)):
		input_size = prev_out_size
		output_size = layers[i]
		network.append(Dense(input_size, output_size))
		network.append(Activation("sigmoid"))
		prev_out_size = output_size
	
	#actual processing
	input_size = prev_out_size
	output_size = 2 #follow picture in pdf, they used 2 neurons in last layer
	network.append(Dense(input_size, output_size))
	network.append(Activation("softmax"))

	return network


def binary_crossentropy_error(y_pred, y_true):
	epsilon = 1e-15 #to prevent division by 0
	loss = -np.mean(y_true * np.log(y_pred + epsilon))
	return loss


def train(network, train_data, train_results, epochs, learning_rate):
	#use stochastic gradient descend for now cuz its easier

	loss_arr = [] #track loss / error after each epoch to plot later
	for epoch in range(epochs):
		error_arr = [] #track error after each iteration

		for i in range(len(train_data)):
			x = train_data[i]
			correct_result = np.array([[1],[0]]) if train_results[i] == "B" else np.array([[0],[1]]) #python op

			#forward part
			output = x.reshape(-1, 1) #need to transpose cuz need convert it to column vector
			for layer in network:
				output = layer.forward(output)
			
			#calculate loss
			error = binary_crossentropy_error(output, correct_result)
			error_arr.append(error)

			#backward
			gradient = output - correct_result

			for layer in reversed(network):
				gradient = layer.backward(gradient, learning_rate)

		loss = np.mean(error_arr)
		loss_arr.append(loss)
		print(f"{epoch + 1}/{epochs} - loss: {loss}")
	
	return loss_arr


def plot_loss(error_arr):
	plot.plot(range(len(error_arr)), error_arr)
	plot.xlabel('Epoch')
	plot.ylabel('loss')
	plot.title('loss graph')
	plot.show()


if __name__ == "__main__":
	try:
		#parsing args
		args = pd.parse_args()
		train_file = args.trainFile
		output_file = args.outputFile
		layers = args.layer #2d array smth like [24,24]
		epochs = args.epochs
		learning_rate = args.learningRate

		#extract and process data
		given_file_contents = pd.readfile(train_file)
		actual_results, data = pd.process_train_contents(given_file_contents)
		data = np.array(data)  #convert list to numpy array
		means, stds = pd.normalise_data(data)

		#training
		network = construct_network(data, layers)
		loss_arr = train(network, data, actual_results, epochs, learning_rate)
		plot_loss(loss_arr)


	except Exception as e:
		print("Error: ", e)
		import traceback
		traceback.print_exc()