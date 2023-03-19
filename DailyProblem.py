#Cyclically Rotate an Array by One 

def Rotate_array(arr,n):
    last = arr[-1]
    for i in range(n-1):
        if i==0:
            temp = arr[i+1]
            arr[i+1] = arr[i]
        arr[0] = last
        if i>0:
            x= arr[i+1]
            arr[i+1] = temp
            temp = x   

    print(arr)

arr = [1,2,3,4,5]
Rotate_array(arr,len(arr))


# t=arr[0]
# p=0
# for i in range(1,len(arr)):
#     p=arr[i]
#     arr[i]=t
#     t=p
# arr[0]=t
# print(arr)
