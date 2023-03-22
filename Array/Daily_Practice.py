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
