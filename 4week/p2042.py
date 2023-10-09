import sys

input = sys.stdin.readline

arr = [0] * 1000001
segTree = [0] * 4000004

def Init(start, end, nodeNum) :
    if start == end :
        segTree[nodeNum] = arr[start]
        return segTree[nodeNum]
    mid = (start + end) // 2
    segTree[nodeNum] = Init(start, mid, nodeNum * 2) + Init(mid + 1, end, nodeNum * 2 + 1)
    return segTree[nodeNum]

def subSum(start, end, nodeNum, left, right) :
    if left > end or right < start :
        return 0
    
    if left <= start and right >= end :
        return segTree[nodeNum]
    mid = (start + end) // 2
    return subSum(start, mid, nodeNum * 2, left, right) + subSum(mid + 1, end, nodeNum * 2 + 1, left, right)

def update(start, end, nodeNum, targetIdx, val) :
    if targetIdx < start or targetIdx > end :
        return
    
    segTree[nodeNum] += val
    if start == end :
        return
    mid = (start + end) // 2
    update(start, mid, nodeNum * 2, targetIdx, val)
    update(mid + 1, end, nodeNum * 2 + 1, targetIdx, val)

n,m,k = map(int, input().split())

for i in range(n) :
    arr[i] = int(input())
    
Init(0, n - 1, 1)

for i in range(m + k) :
    a,b,c = map(int,input().split())
    if a == 1 :
        tmp = c - arr[b - 1]
        arr[b - 1] = c
        update(0, n - 1, 1, b - 1, tmp)
    else :
        print(subSum(0, n - 1, 1, b - 1, c - 1))