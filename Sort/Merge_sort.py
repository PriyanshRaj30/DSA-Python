def Merge_sort(arr):
    if len(arr)==1:
        return
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    Merge_sort(left)
    Merge_sort(right)
    Merge_2sorted_arr(left,right,arr)

def Merge_2sorted_arr(a,b,arr):
    i = j = k = 0
    while i <len(a) and j <len(b):
        if a[i] <= b[j]:
            arr[k] = a[i]
            i +=1
        else:
            arr[k] = b[j]
            j +=1
        k+=1

    while i <len(a):
        arr[k] = a[i]
        k+=1
        i+=1
    while j <len(b):
        arr[k] = b[j]
        k+=1
        j+=1




arr = [2,1,3,7,5,4]
Merge_sort(arr)
print(arr)
