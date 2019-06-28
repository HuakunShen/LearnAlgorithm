from IsSorted import *
def merge_sort(arr):
	''' Merge arr in non-decreasing order '''
	# Base Case
	if len(arr) <= 1:
        return
    
    # Divide and Conquer
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    merge_sort(left)
    merge_sort(right)

	# Merge (Generate) final solution
    merge(arr, left, right)


def merge(arr, left, right):
	''' Merge Two Sorted Array into One Sorted Array '''
    i = j = num = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[num] = left[i]
            i += 1
        else:
            arr[num] = right[j]
            j += 1
        num += 1

    if i < len(left):
        arr[num:] = left[i:]
    if j < len(right):
        arr[num:] = right[j:]


if __name__ == "__main__":
	# test
	
	import random
	test_times = 100
	test_len = 100
	for i in range(test_times):
		arr = []
		for j in range(test_len):
			arr.append(random.randint())
		merge_sort(arr)
		if not is_sorted(arr):
			print("Test Failed")
			break
	print("Test Passed with ", test_times, " tests of length ", test_len)
	
	
	
	
	
	
	
	
	
	
	
