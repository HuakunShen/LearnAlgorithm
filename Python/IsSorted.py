def is_sorted(arr: list):
	for i in range(len(arr) - 1):
		if arr[i] > arr[i + 1]:
			return False
	return True

def is_sorted_disp(arr: list):
	for i in range(len(arr) - 1):
		if arr[i] > arr[i + 1]:
			print("Given input is not sorted.")
			return False
	print("Given input is sorted.")
	return True
