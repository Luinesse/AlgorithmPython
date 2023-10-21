n = int(input())
m = int(input())

res = 0

visited = [0] * 101
graph = dict()

def dfs(start) :
    global res
    if visited[start] == 0 :
        visited[start] = 1
    
    if start in graph :
        next = list(graph[start])
    else :
        return
        
    for i in range(len(next)) :
        value = next[i]
        if visited[value] == 0 :
            visited[value] = 1
            res += 1
            dfs(value)

for i in range(m) :
    a, b = map(int, input().split())
    
    if a in graph :
        graph[a].add(b)
    else :
        graph[a] = {b}
    if b in graph :
        graph[b].add(a)
    else :
        graph[b] = {a}

dfs(1)
print(res)