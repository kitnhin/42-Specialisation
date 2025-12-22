import sys
import math
import utils.data_loader as dl
import utils.maths_fts as mf

import json

#variables
file_contents = ""
field_values = []
field_names = []

#student variables
student_houses = []
student_scores = [] #courses: Astro, Herb, Divination, Muggle, AncientR, History, Trans, Potions, Charms, Flying

#weights
weights = {}
weights["Gryffindor"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
weights["Slytherin"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
weights["Ravenclaw"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
weights["Hufflepuff"] = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

#getting data
def extract_student_data():
	global student_houses, student_scores

	#extract the indexes
	house_index = field_names.index("Hogwarts House")
	course_indices = [
		field_names.index("Astronomy"), field_names.index("Herbology"), field_names.index("Divination"),
		field_names.index("Muggle Studies"), field_names.index("Ancient Runes"), field_names.index("History of Magic"),
		field_names.index("Transfiguration"), field_names.index("Potions"), field_names.index("Charms"), field_names.index("Flying")
	]
	
	num_students = len(field_values[0])
	
	for i in range(num_students):
		house = field_values[house_index][i].strip()

		scores = []
		skip_student = False
		
		for course_idx in course_indices:
			score = field_values[course_idx][i].strip()
			if not score or not house:
				skip_student = True
				break
			scores.append(float(score))
		
		if not skip_student:
			student_houses.append(house)
			student_scores.append(scores)

def normalise_student_score():
	means = []
	stds = []
	num_features = len(student_scores[0])
	num_students = len(student_scores)

	#extract scores for each feature
	for feature_idx in range(num_features):
		feature_values = []
		for student in range(num_students):
			feature_values.append(student_scores[student][feature_idx])
		
		means.append(mf.calc_mean(feature_values))
		stds.append(mf.calc_std(feature_values))
	
	#normalise student scores 
	#equation: (original - mean) / std
	for student_idx in range(num_students):
		for feature_idx in range(num_features):
			original_value = student_scores[student_idx][feature_idx]
			normalised_value = (original_value - means[feature_idx]) / stds[feature_idx]
			student_scores[student_idx][feature_idx] = normalised_value

	return means, stds


#calculations
def calc_confidence(house_name, score):
	#z calculation
	z = weights[house_name][0]
	for i in range(len(score)):
		z += weights[house_name][i + 1] * score[i]

	#normalise to probability (sigmoid calculation, g)
	return 1 / (1 + math.exp(-z))

def calc_cost(house_name):
	num_of_students = len(student_scores)

	total_cost = 0
	for i in range(num_of_students):
		y_term = 1 if student_houses[i] == house_name else 0
		total_cost += y_term * math.log(calc_confidence(house_name, student_scores[i])) 
		+ (1 - y_term) * math.log(1 - calc_confidence(house_name, student_scores[i]))

	average_cost = -(1/num_of_students) * total_cost
	return average_cost

def calc_gradient(house_name):
	num_weights = len(weights[house_name])
	num_students = len(student_scores)
	gradients = [0] * num_weights

	#calculate the sum part
	for i in range(num_students):
		h = calc_confidence(house_name, student_scores[i])
		y = 1 if student_houses[i] == house_name else 0
		
		gradients[0] += h - y #bias

		for j in range(1, num_weights):
			gradients[j] += (h - y)*student_scores[i][j - 1] #student score need j - 1 cuz the first score (astronomy), is for the second weight
		
	#average out the gradients
	for i in range(num_weights):
		gradients[i] /= num_students

	return gradients

def update_weights(house_name, gradients):
	learning_rate = 0.1 #maybe can change ltr
	for i in range(len(weights[house_name])):
		weights[house_name][i] -= learning_rate * gradients[i]

#training loops
def train_house(house_name, iterations):
	for iteration in range(iterations):
		gradients = calc_gradient(house_name)
		update_weights(house_name, gradients)

	final_cost = calc_cost(house_name)
	print(f"House training complete: {house_name} - Final cost: {final_cost}")

def train():
	iterations = 100 #change later if want
	houses = ["Gryffindor", "Slytherin", "Ravenclaw", "Hufflepuff"]
	print("Starting Training...")
	for house in houses:
		train_house(house, iterations)

#output
def save_model(weights, means, stds):
	filename = "params.json"
	data = {
		"weights": weights,
		"means": means,
		"stds": stds
	}
	try:
		f = open(filename, "w")
		f.write(json.dumps(data))
		f.close()
	except Exception:
		print("Failed to save params")


if __name__ == "__main__":
	try:
		if len(sys.argv) != 2:
			raise Exception("Invalid number of arguments")
		
		file_contents = dl.readfile(sys.argv[1])
		field_names, field_values = dl.extract_fields(file_contents)
		extract_student_data()
		means, stds = normalise_student_score()
		train()
		save_model(weights, means, stds)

		
	except Exception as e:
		print("Error: ", e)