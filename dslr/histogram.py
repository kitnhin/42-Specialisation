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
	
	#init the subplot
	num_of_columns = 5
	num_of_rows = math.ceil(len(numeric_fields_index) / num_of_columns)
	fig, axes = plot.subplots(num_of_rows, num_of_columns, figsize=(15, len(numeric_fields_index)*0.6)) #figsize is the total figure size so idh to always zoom
	axes = axes.flatten() #axes is a 2d array of plot objects, flatten makes it 1D so i can access it easier
	plot.subplots_adjust(hspace=0.5, wspace=0.6) #set spacing between plots

	best_score = 999999999999
	best_course = ""
	best_course_index = 0
	for i in range(len(numeric_fields_index)):
		score = plot_histogram(field_values[numeric_fields_index[i]], field_names[numeric_fields_index[i]], axes[i])
		if score < best_score:
			best_course = field_names[numeric_fields_index[i]]
			best_score = score
			best_course_index = numeric_fields_index[i]
	plot.show()

	fig2, ax2 = plot.subplots(1, 1, figsize=(10, 6))
	plot_histogram(field_values[best_course_index], best_course, ax2)
	ax2.set_title("Best course: " + best_course)
	ax2.legend()
	plot.show()


def plot_histogram(field, fieldname, axes):

	#find house index
	house_index = -1
	for i in range(len(field_names)):
		if field_names[i].lower() == "hogwarts house":
			house_index = i
			break

	# Extract scores
	house_names = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
	colors = ['red', 'green', 'blue', 'yellow']
	house_scores = []
	for i in range(4):
		house_scores.append([])

	for i in range(len(field)):
		if field[i].strip() == "":
			continue
		house = field_values[house_index][i].strip()
		score = float(field[i].strip())
		for h in range(4):
			if house == house_names[h]:
				house_scores[h].append(score)
				break

	#plot for each house
	for h in range(4):
		axes.hist(house_scores[h], alpha=0.5, color=colors[h], label=house_names[h])

	axes.set_xlabel("Scores")
	axes.set_ylabel("Frequency")
	axes.set_title(fieldname)

	# calculate the std diff so we know which course have the closest score
	house_stds = []
	for h in range(4):
		std = calc_std(house_scores[h])
		house_stds.append(std)

	average_std = sum(house_stds) / 4

	total_difference = 0
	for std in house_stds:
		difference = abs(std - average_std)
		total_difference += difference

	score = total_difference / 4
	return score

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