import sys
input = sys.stdin.readline

n = int(input())

lines = [] * n

for i in range(n) :
    x, y = map(int, input().split())
    pair = (x, y)
    lines.append(pair)

lines.sort(key= lambda k : k[0])

start = lines[0][0]
end = lines[0][1]
res = 0

for i in range(n) :
    if lines[i][0] > end :
        res += end - start
        start = lines[i][0]
        end = lines[i][1]
    else :
        end = max(end, lines[i][1])

res += end - start
print(res)