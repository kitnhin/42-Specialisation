import sys
import math
import numpy as np
import matplotlib.pyplot as plot

#variables
file_contents = ""
field_values = []
field_names = []

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
	global field_values, number_of_fields, field_names

	#extract field names
	lines = file_contents.split('\n')
	field_names = lines[0].split(",")
	number_of_fields = len(field_names)

	#init fields
	for i in range(number_of_fields):
		field_values.append([])

	# extract the rest of the fields
	for i in range(1, len(lines)):
		line_parts = lines[i].split(",")
		if len(line_parts) == number_of_fields:
			for j in range(number_of_fields):
				field_values[j].append(line_parts[j])

def readfile(filename):
	global file_contents
	file = open(filename)
	file_contents = file.read()
	file.close()

def calc_and_display_histogram():

	#find the numberic fields
	numeric_fields_index = []
	for i in range(1, len(field_values)):
		if(check_array_is_numeric(field_values[i]) == True):
			numeric_fields_index.append(i)
	
	


def calc_correlation(field1, field2):
	#convert the fields to number arr
	field1_nums = []
	field2_nums = []
	for i in range(len(field1)):
		if field1.strip() != "":
			field1_nums.append(float(field1[i].strip()))
		if field2.strip() != "":
			field2_nums.append(float(field2[i].strip()))
	

#calc functions
def calc_min(values):
	min_value = 2**63

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

def calc_count(values):
	count = 0
	for i in range(len(values)):
		count += 1
	return count

def calc_mean(values):
	sum = 0
	for i in range(len(values)):
		sum += values[i]
	mean = sum / calc_count(values)
	return mean

def calc_std(values):
	mean = calc_mean(values)
	std = 0
	for i in range(len(values)):
		std += (values[i] - mean) ** 2
	
	std = math.sqrt(std / calc_count(values))
	return std


if __name__ == "__main__":
	try:
		if len(sys.argv) != 2:
			raise Exception("Invalid number of arguments")
		
		readfile(sys.argv[1])
		extract_fields()
		calc_and_display_histogram()

	except Exception as e:
		print("Error: ", e)