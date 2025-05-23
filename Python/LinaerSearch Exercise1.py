def linear_search(arr, target):
    for i in range(len(arr)):
        if (arr[i] == target):
            return i
    return -1
arr = [34, 23, 1, 56, 89, 12, 65]
target=int(input("Enter the number to search:"))
result=linear_search(arr, target)
if result!= -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")
               
