city = [0] * 201
res = [0] * 1001

def find(key) :
    if key == city[key] :
        return key
    else :
        city[key] = find(city[key])
        return city[key]
    
def union(a, b) :
    ta = find(a)
    tb = find(b)
    
    if ta != tb :
        city[ta] = tb

n = int(input())
m = int(input())

for i in range(1, 201) :
    city[i] = i

for i in range(1, n + 1) :
    arr = list(map(int, input().split()))
    for k in range(1, n + 1) :
        if arr[k - 1] == 1 :
            union(i,k)

prev = 0
tmp = list(map(int, input().split()))
for i in range(1, m + 1) :
    res[i] = find(tmp[i - 1])
    if i == 1 :
        prev = find(tmp[i - 1])
    else :
        if prev != res[i] :
            print("NO")
            exit()

print("YES")