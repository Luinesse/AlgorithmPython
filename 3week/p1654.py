def isPos(arr, n, mid, tar) :
    tmp = 0
    for i in range(n) :
        tmp += arr[i] // mid
    return (tmp >= tar)

def binarySearch(arr, n, end, tar) :
    left = 1
    right = end

    while left <= right :
        mid = (left + right) // 2
        if(isPos(arr,n,mid,tar)) :
            left = mid + 1
        else :
            right = mid - 1
    return left - 1

k, n = map(int, input().split())

max = 0
arr = []

for i in range(k) :
    tmp = int(input())
    if max < tmp :
        max = tmp
    arr.append(tmp)

print(binarySearch(arr,k,max,n))