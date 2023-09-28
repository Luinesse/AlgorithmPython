def binarySearch(arr, start, end, target) :
    mid = 0
    
    while(start < end) :
        mid = (start + end) // 2
        if(arr[mid] < target) :
            start = mid + 1
        else :
            end = mid
    
    return start

idx = 0
n = int(input())
extra = list(map(int,input().split()))
arr = [0] * n

for i in range(n) :
    if i == 0 : arr[0] = extra[0]
    
    if extra[i] > arr[idx] :
        idx += 1
        arr[idx] = extra[i]
    else :
        arr[binarySearch(arr,0,idx,extra[i])] = extra[i]
        
print(idx + 1)