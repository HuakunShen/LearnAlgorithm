from isSorted import *


def merge_sort(arr: list):
	''' Sort input array in non-decreasing order '''
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


def merge(arr: list, left, right):
	''' Merge two sorted arrays into one sorted array '''
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
    sorted_test(100, 100, merge_sort)

