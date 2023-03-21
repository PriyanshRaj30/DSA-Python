def Find_min_and_max(arr,n):
    Max = arr[0]
    Min = arr[0]
    for i in range(n):
        if Max < arr[i]:
            Max = arr[i]
        elif Min > arr[i]:
            Min = arr[i]
    print("Max Element ==> ",Max)
    print("Min Element ==> ",Min)

array = [1,5,0,2,3,6,4,2,1]
n = len(array)
Find_min_and_max(array,n)
