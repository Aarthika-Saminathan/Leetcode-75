def move_zeros(arr):
    non_zero=0
    for i in range (len(arr)):
        if arr[i]!=0:
            arr[non_zero],arr[i]=arr[i],arr[non_zero]
            non_zero+=1
    return arr

arr=[1,0,0,7,8]
print(move_zeros(arr))