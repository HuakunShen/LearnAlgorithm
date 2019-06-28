from IsSorted import *
def merge_sort(arr):
    if len(arr) <= 1:
        return
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge(arr, left, right)


def merge(arr, left, right):
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
    arr = [7, 4, 9, 8, 1]
    merge_sort(arr)
    is_sorted_disp(arr)
    print(is_sorted(arr))
