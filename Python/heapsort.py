import isSorted
import util

def heap_sort(arr: list):
	tmp = []
	
	
def parent(index: int):
	return index // 2
	

def left_child(index: int):
	return 2 * index
	

def right_child(index: int):
	return 2 * index + 1

	
def min_heapify(arr, index):
	left = left_child(index)
	right = right_child(index)
	if left <= len(arr) and arr[left] < arr[index]:
		smallest = left
	else:
		smallest = index
	if left <= len(arr) and arr[left] < arr[smallest]:
		smallest = right
	if smallest != index:
		util.swap(arr, index, smallest)
		min_heapify(arr, smallest)
		
		
def build_min_heap(arr):
	arr
		
		
		
		
		
		
		
		
		

isSorted.sorted_test(100, 100, heap_sort())
