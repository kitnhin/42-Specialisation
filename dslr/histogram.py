import sys
import math
import numpy as np
import matplotlib.pyplot as plot

#variables
file_contents = ""
fields = []
field_names = []
number_of_bars = 30

# flag = 1

def is_numeric(str):
	try:
		float(str.strip())
		return True
	except:
		return False
	
def check_array_is_numeric(arr):
	found_value = False
	for i in range(len(arr)):

		if arr[i].strip() == "":
			continue

		found_value = True

		if is_numeric(arr[i]) == False:
			# print(arr[i], "is not numeric")
			return False
	
	return found_value # if all are empty strings then auto will return false

def extract_fields():
	global fields, number_of_fields, field_names

	#extract field names
	lines = file_contents.split('\n')
	field_names = lines[0].split(",")
	number_of_fields = len(field_names)

	#init fields
	for i in range(number_of_fields):
		fields.append([])

	# extract the rest of the fields
	for i in range(1, len(lines)):
		line_parts = lines[i].split(",")
		if len(line_parts) == number_of_fields:
			for j in range(number_of_fields):
				fields[j].append(line_parts[j])


def readfile(filename):
	global file_contents
	file = open(filename)
	file_contents = file.read()
	file.close()

def calc_values_and_print():
	
	#find the numberic fields
	numeric_fields_index = []
	for i in range(1, len(fields)):
		if(check_array_is_numeric(fields[i]) == True):
			numeric_fields_index.append(i)
	
	#init the subplot
	num_of_columns = 5
	num_of_rows = math.ceil(len(numeric_fields_index) / num_of_columns)
	fig, axes = plot.subplots(num_of_rows, num_of_columns, figsize=(15, len(numeric_fields_index)*0.7)) #figsize is the total figure size so idh to always zoom
	axes = axes.flatten() #axes is a 2d array of plot objects, flatten makes it 1D so i can access it easier
	plot.subplots_adjust(hspace=0.5, wspace=0.6) #set spacing between plots

	for i in range(len(numeric_fields_index)):
		plot_histogram(fields[numeric_fields_index[i]], field_names[numeric_fields_index[i]], axes[i])
	
	plot.show()

def plot_histogram(field, fieldname, axes):

	numeric_values = convert_field_to_int(field)

	# find the range of each bar
	max_value = calc_max(field)
	min_value = calc_min(field)
	bar_width = (max_value - min_value) / number_of_bars

	#find the counts of each range
	counts = [0] * number_of_bars
	for i in range(len(numeric_values)):
		bar_index = int((numeric_values[i] - min_value) / bar_width)
		
		if bar_index >= number_of_bars: # only happens at max_value
			bar_index = bar_index - 1
			
		counts[bar_index] += 1
	
	# meng plot kan
	for i in range(number_of_bars):
		left_edge = bar_width * i + min_value
		axes.bar(left_edge, counts[i], width=bar_width, align="edge")
	
	axes.set_xlabel("Scores")
	axes.set_ylabel("Frequency")
	axes.set_title(fieldname)

def calc_min(values):
	min_value = 2**63   # 9223372036854775808 (64bit int min cuz python has no min wts)

	for i in range(len(values)):
		if values[i].strip() == "":
			continue
		min_value = min(min_value, float(values[i]))
	
	return min_value

def calc_max(values):
	max_value = -2**63

	for i in range(len(values)):
		if values[i].strip() == "":
			continue
		max_value = max(max_value, float(values[i]))
	
	return max_value

def convert_field_to_int(field):
	numeric_values = []
	for value in field:
		if value.strip() != "":
			numeric_values.append(float(value.strip()))
	return numeric_values


if __name__ == "__main__":
	try:
		if len(sys.argv) != 2:
			raise Exception("Invalid number of arguments")
		
		readfile(sys.argv[1])
		extract_fields()
		calc_values_and_print()

	except Exception as e:
		print("Error: ", e)