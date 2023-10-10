import sys
sys.setrecursionlimit(10**6)

n = int(input())
inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))
tmp = [0] * 100001

for i in range(n) :
    tmp[inOrder[i]] = i

def preOrder(inFirst, inEnd, postFirst, postEnd) :
    if inFirst > inEnd or postFirst > postEnd :
        return
    root = postOrder[postEnd]
    idx = tmp[root]
    leftLength = idx - inFirst
    
    print(root, end=" ")
    
    preOrder(inFirst, idx - 1, postFirst, postFirst + leftLength - 1)
    preOrder(idx + 1, inEnd, postFirst + leftLength, postEnd - 1)

preOrder(0, n - 1, 0, n - 1)