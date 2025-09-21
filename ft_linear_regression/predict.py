import json

theta0 = 0
theta1 = 0

def get_theta():
	global theta0, theta1
	file = open("params.json", "r")
	params_obj = json.load(file)
	theta0 = params_obj["theta0"]
	theta1 = params_obj["theta1"]

def estimate_price(milage):
	return theta0 + theta1 * milage

if __name__ == "__main__":
	get_theta()

	milage_string = input("Enter your milage: ")
	result = estimate_price(float(milage_string))
	if float(milage_string) < 10000:
		print("Result might be inaccurate because milage given is too small")
	print(f"Price for milage: ${milage_string}km is ${result}")
