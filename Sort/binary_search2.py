#this is a literative method
def Binary_search(arr,x):
    right = len(arr) -1
    left = 0
   
    while left<=right:
        
        mid = (right + left)//2
        if x < arr[mid]:
            right = mid - 1
        
        elif x > arr[mid]:
            left = mid + 1
        else:
            return f"The position of the number is {mid}"

    return -1


arr = [1,2,3,4,5,6]
x = 2
print(Binary_search(arr,x))
