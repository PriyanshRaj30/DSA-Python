#Given an array of N integers arr[] where each element represents the maximum length of the jump that can be made forward from that element.
#This means if arr[i] = x, then we can jump any distance y such that y ≤ x.
#Find the minimum number of jumps to reach the end of the array

def minJumps(arr):
    pointer  = 0
    count = 0
    for i in range(len(arr)):
        if i == pointer:
            pointer = arr[i+1]
            count +=1
    return count

arr = [1,3,5,8,9,2,6,7,6,8,9]
print(minJumps(arr))
