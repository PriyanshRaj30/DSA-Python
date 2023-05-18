def Insertion_sort(arr):
    for i in range(1,len(arr)):
        j = i 
        while arr[j-1] > arr[j] and j>0:
            arr[j-1],arr[j] = arr[j],arr[j-1]
            j -=1
    print(arr)

arr = [3,2,5,4,7,6,1,8,0]

Insertion_sort(arr)
