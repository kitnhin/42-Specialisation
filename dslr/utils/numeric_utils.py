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
