import sys
import math
import numpy as np
import matplotlib.pyplot as plot
import utils.data_loader as dl
import utils.maths_fts as mf
import utils.numeric_utils as nu

#variables
file_contents = ""
field_values = []
field_names = []

#student variables
student_houses = []
student_scores = [] #courses: Astro, Herb, Divination, Muggle, AncientR, History, Trans, Potions, Charms, Flying

def extract_student_data():

	global student_houses, student_scores

	#extract the indexes
	house_index = field_names.index("Hogwarts House")
	course_indices = [
		field_names.index("Astronomy"), field_names.index("Herbology"), field_names.index("Defense Against the Dark Arts"),
		field_names.index("Divination"), field_names.index("Muggle Studies"), field_names.index("Ancient Runes"), field_names.index("History of Magic"),
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


if __name__ == "__main__":
	try:
		if len(sys.argv) != 2:
			raise Exception("Invalid number of arguments")
		
		file_contents = dl.readfile(sys.argv[1])
		field_names, field_values = dl.extract_fields(file_contents)
		extract_student_data()
		print(student_houses[:2])
		print(student_scores[:2])
	except Exception as e:
		print("Error: ", e)