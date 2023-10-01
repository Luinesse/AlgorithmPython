import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split(" ")))
x = int(sys.stdin.readline())
res = 0

arr.sort()

lp = 0
rp = n - 1

while(lp < rp) :
    if arr[lp] + arr[rp] < x :
        lp += 1
    elif arr[lp] + arr[rp] > x :
        rp -= 1
    else :
        lp += 1
        rp -= 1
        res += 1

print(res)