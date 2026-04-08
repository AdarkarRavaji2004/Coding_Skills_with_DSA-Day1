def binarySearch(arr, target):
    start = 0
    end = len(arr)-1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]<target:
            start = mid+1
        else:
            end = mid-1
    return -1

sortedArray = [1,2,3,4,5,6,7,8,9]
target = 8
result = binarySearch(sortedArray, target)
if result == -1:
    print("Element Not Found") 
else:
    print("Element found at index ",result)