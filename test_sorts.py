import pytest


def bubble_sort(nums):
    swapped = True
    while swapped:
        swapped = False
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
               swapped = True
               nums[i], nums[i+1] = nums[i+1], nums[i]


def test_bubble_sort():
    nums = [3,6,2,6,4,7,8]

    bubble_sort(nums)

    sorted_nums = sorted(nums[:])
    assert nums == sorted_nums


def selection_sort(nums):
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                nums[i], nums[j] = nums[j], nums[i]


def test_selection_sort():
    nums = [3, 6, 2, 6, 4, 7, 8]

    selection_sort(nums)

    sorted_nums = sorted(nums[:])
    assert nums == sorted_nums


def merge_sort(nums):
    if len(nums) <= 1:
        return

    length_nums = len(nums)
    middle = length_nums // 2

    l = nums[:middle]
    r = nums[middle:]

    merge_sort(l)
    merge_sort(r)

    i = j = k = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            nums[k] = l[i]
            i += 1
        else:
            nums[k] = r[j]
            j += 1

        k += 1

    while i < len(l):
        nums[k] = l[i]
        i += 1
        k += 1

    while j < len(r):
        nums[k] = r[j]
        j += 1
        k += 1


def test_merge_sort():
    nums = [3, 6, 2, 6, 4, 7, 8]
    sorted_nums = sorted(nums[:])

    merge_sort(nums)

    assert nums == sorted_nums


def partition(nums, low, high):
    i = low-1
    pivot = nums[high]

    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i+1], nums[high] = nums[high], nums[i+1]

    return i+1

def quick_sort(nums, low, high):
    if low < high:
        p = partition(nums, low, high)

        quick_sort(nums, low, p-1)
        quick_sort(nums, p+1, high)


def test_quick_sort():
    nums = [3, 6, 2, 6, 4, 7, 8]
    sorted_nums = sorted(nums[:])

    quick_sort(nums, 0, len(nums)-1)

    assert nums == sorted_nums


def bin_search_recursive(nums, num_to_find, low, high):
    mid = low + (high - low) // 2

    if nums[mid] == num_to_find:
        return mid

    if nums[mid] < num_to_find:
        return bin_search_recursive(nums, num_to_find, mid, high)

    if nums[mid] > num_to_find:
        return bin_search_recursive(nums, num_to_find, low, mid)


def test_bin_search_recursive():
    nums = [i for i in range(100)]

    num_to_find = 23

    index = bin_search_recursive(nums, num_to_find, 0, len(nums)-1)

    assert index == num_to_find


def bin_search_loop(nums, num_to_find):
    low = 0
    high = len(nums) - 1

    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] == num_to_find:
            return mid
        elif nums[mid] < num_to_find:
            low = mid
        elif nums[mid] > num_to_find:
            high = mid


def test_bin_search_loop():
    nums = [i for i in range(100)]

    num_to_find = 23

    index = bin_search_loop(nums, num_to_find)

    assert index == num_to_find
