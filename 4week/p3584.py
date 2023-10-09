import sys
sys.setrecursionlimit(10**4)

def setDepth(a, parent, depth) :
    if parent[a] == 0 :
        return
    else :
        setDepth(parent[a], parent, depth)
        depth[a] = depth[parent[a]] + 1

def LCA(x, y, parent, depth) :
    while depth[x] > depth[y] :
        x = parent[x]
    
    while depth[x] < depth[y] :
        y = parent[y]
        
    while x != y :
        x = parent[x]
        y = parent[y]
        
    return x

parent = [0] * 10001
depth = [1] * 10001

t = int(input())

for i in range(t) :
    n = int(input())
    for k in range(n - 1) :
        a, b = map(int, input().split())
        parent[b] = a
    
    for k in range(1, n + 1) :
        setDepth(k,parent,depth)
        
    t1, t2 = map(int, input().split())
    
    print(LCA(t1, t2, parent, depth))
    
    for k in range(10001) :
        parent[k] = 0
        depth[k] = 1