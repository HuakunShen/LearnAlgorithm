def quick_sort(arr):
    if len(arr) <= 1:
        return
    pivot = arr[0]
    small = []
    large = []
    for i in range(1, len(arr)):
        if arr[i] < pivot or arr[i] == pivot:
            small.append(arr[i])
        else:
            large.append(arr[i])
            
    quick_sort(small)
    quick_sort(large)
    result = small + [pivot] + large
    arr[:] = result[:]
    
if __name__ == "__main__":
	arr = [3, 5, 1, 4, 2]
	quick_sort(arr)
	print(arr)
