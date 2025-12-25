import argparse

def readfile(filename):
	file = open(filename)
	file_contents = file.read()
	file.close()
	return file_contents

def parse_args():

	#python argument parser very nice(type defaults to string)
	parser = argparse.ArgumentParser()
	parser.add_argument('--givenFile', default="datasets/data-2.csv")
	parser.add_argument('--trainFile', default="datasets/dataset_train.csv")
	parser.add_argument('--predictFile', default="datasets/dataset_predict.csv")
	parser.add_argument('--trainPercentage', type=float, default=0.7)

	return parser.parse_args()

def write_data(data, filename):
	try:
		f = open(filename, "w")
		f.write("\n".join(data)) #join 2d array to a string, as write only works for strings
		f.close()
	except Exception:
		print("Failed to write data")

if __name__ == "__main__":
	try:
		#parsing args
		args = parse_args()
		given_file = args.givenFile
		train_percentage = args.trainPercentage
		train_file = args.trainFile
		predict_file = args.predictFile

		#read file
		given_file_contents = readfile(given_file)
		
		#calculate lines
		lines = given_file_contents.strip().split("\n")
		number_of_lines = len(lines)
		train_lines = int(number_of_lines * train_percentage)

		#write
		write_data(lines[:train_lines], train_file)
		write_data(lines[train_lines:], predict_file)
		

	except Exception as e:
		print("Error: ", e)