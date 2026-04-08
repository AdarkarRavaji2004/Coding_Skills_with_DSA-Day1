def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target element
    return -1  # Return -1 if the target element is not found

array = [1,2,3,4,5,6,7,8,9]
target = 55
result = linearSearch(array, target)
if result != -1:
    print(f"Element {target} found at index: {result}") 
else:
    print(f"Element {target} not found in the array.")