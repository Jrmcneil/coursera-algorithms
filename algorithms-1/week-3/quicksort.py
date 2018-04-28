import math

def quicksort(array):
    sorted_array = array
    comparisons = recursively_partition(sorted_array, 0, len(array) - 1)
    print("Comparisons")
    print(comparisons)
    return sorted_array


def recursively_partition(array, left, right):
    if right - left < 1:
        return 0

    pivot = choose_pivot(array, left, right)
    i = left + 1
    for j in range(left + 1, right + 1):
        if array[j] < pivot:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
            i += 1
    array[left] = array[i - 1]
    array[i - 1] = pivot
    left_comparisons = recursively_partition(array, left, i - 2)
    right_comparisons = recursively_partition(array, i, right)
    return left_comparisons + right_comparisons + right - left


# Using left most index as pivot
# def choose_pivot(array, left, right):
#     return array[left]


# Using the right most index as the pivot
# def choose_pivot(array, left, right):
#     swap_pivot(array, left, right)
#     return array[left]


# Using the median of three as the pivot
def choose_pivot(array, left, right):
    middle = left + int(math.ceil((right - left - 1)/2))
    if is_median(array, middle, left, right):
        swap_pivot(array, left, middle)
    if is_median(array, right, middle, left):
        swap_pivot(array, left, right)
    return array[left]


def is_median(array, test, a, b):
    return (array[a] <= array[test] <= array[b]) or (array[b] <= array[test] <= array[a])


def swap_pivot(array, left, index):
    pivot = array[index]
    array[index] = array[left]
    array[left] = pivot


def run():
    with open('./quicksort-data.txt') as f:
        data = ([int(line) for line in f])
        quicksort(data)


def run_test():
    with open('./test-data.txt') as f:
        data = ([int(line) for line in f])
        quicksort(data)