def binarySearch(arr, end, target) :
    left = 0
    right = end - 1
    
    while(left <= right) :
        mid = (left + right) // 2
        if(arr[mid] < target) :
            left = mid + 1
        elif(arr[mid] > target) :
            right = mid - 1
        else :
            return 1
    return 0

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()

for i in range(m) :
    print(binarySearch(a, n, b[i]))
