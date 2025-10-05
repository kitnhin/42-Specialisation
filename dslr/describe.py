import sys
import math
import numpy as np

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
			return False
	
	return found_value # if all are empty strings then auto will return false

def extract_fields():
	global field_values, field_names

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

def calc_values_and_print():

	#printing settings
	print_field_size = 30
	pad_number = 10

	#print header
	headings = ["field", "count", "mean", "std", "min", "25%", "50%", "75%", "max"]
	for i in range(len(headings)):
		if i == 0:
			print(f"|{headings[i]:^{print_field_size}}|", end = "") # template string (:^ means centre alignment padding, so :^10 means fit element in a 10 space area wif center alighnment)
		else:
			print(f"|{headings[i]:^{pad_number}}|", end = "")
	print(f"\n{(print_field_size + ((pad_number + 1) * len(headings))) * "-"}")

	
	for i in range(1, len(field_values)):
		#print field name
		print(f"|{field_names[i]:<{print_field_size}}|", end="") # :< means left alighnment

		#print number
		if(check_array_is_numeric(field_values[i]) == True):

			#append calculations here and it shall be auto added
			stats_calculated = []
			stats_calculated.append(calc_count(field_values[i]))
			stats_calculated.append(calc_mean(field_values[i]))
			stats_calculated.append(calc_std(field_values[i]))
			stats_calculated.append(calc_min(field_values[i]))
			stats_calculated.append(calc_percentile(field_values[i], 25))
			stats_calculated.append(calc_percentile(field_values[i], 50))
			stats_calculated.append(calc_percentile(field_values[i], 75))
			stats_calculated.append(calc_max(field_values[i]))

			for i in range(len(stats_calculated)):
				print(f"|{truncate_number(stats_calculated[i], pad_number):^{pad_number}}|", end="")
			print("")

		else:
			print("| No values for this field")

def truncate_number(number, pad_number):
	rounded = round(number, 2) # limit 2 decimal places
	number_str = str(rounded)
	if len(number_str) > pad_number:
		number_str = number_str[:7] + "..."
	return number_str
				

# calculation functions
def calc_count(values):
	count = 0
	for i in range(len(values)):
		if values[i].strip() == "":
			continue
		count += 1
	return count

def calc_mean(values):
	sum = 0
	for i in range(len(values)):
		if values[i].strip() == "":
			continue
		sum += float(values[i])
	mean = sum / calc_count(values)
	return mean

def calc_std(values):
	mean = calc_mean(values)
	std = 0
	for i in range(len(values)):
		if values[i].strip() == "":
			continue
		std += (float(values[i]) - mean) ** 2
	
	std = math.sqrt(std / calc_count(values))
	return std

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

def calc_percentile(values, percentile):

	# convert all values to numbers
	numbers = []
	for i in range(len(values)):
		if values[i].strip() == "":
			continue
		numbers.append(float(values[i]))
		
	# return np.percentile(numbers, 50)
	# steps:
	# 1) sort numbers
	# 2) find pos (number of elements - 1) * (percentile / 100) (n - 1 to take into account index starts from 0)
	# 3) pos is most likely a float, so need interpolation ( small + (big - small) * fractional part of pos)
	# for step 3: if pos = 3.5, small = numbers[3] and big = numbers[4]

	sorted_numbers = sorted(numbers)
	n = calc_count(values)
	pos = (n - 1) * (percentile / 100)
	lower_index = int(math.floor(pos))
	upper_index = int(math.ceil(pos))
	fraction = pos - lower_index

	#interpolation
	nth_percentile_value = sorted_numbers[lower_index] + fraction * (sorted_numbers[upper_index] - sorted_numbers[lower_index])
		
	return nth_percentile_value


if __name__ == "__main__":
	try:
		if len(sys.argv) != 2:
			raise Exception("Invalid number of arguments")
		
		readfile(sys.argv[1])
		extract_fields()
		calc_values_and_print()

	except Exception as e:
		print("Error: ", e)