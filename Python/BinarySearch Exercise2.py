def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # This should be outside the while loop

arr = [10, 20, 30, 40, 50, 60]
target = int(input("Enter number to search: "))
result = binary_search(arr, target)
if result != -1:
    print(f"{target} found at index {result}")
else:
    print(f"{target} not found in the list")

