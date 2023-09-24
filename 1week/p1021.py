stack = []
def addLast(n) :
    stack.append(n)

def addFirst(n) :
    stack.insert(0, n)
    
def removeLast() :
    stack.pop(-1)

def removeFirst() :
    stack.pop(0)

def front() :
    return stack[0]

def back() :
    tmp = len(stack)
    return stack[tmp - 1]

n, m = map(int, input().split())
tmp = list(map(int, input().split()))
res = 0
idx = 0
listIdx = 0

for i in range(n) :
    addLast(i + 1)

while True :
    for i in range(len(stack)) :
        if tmp[listIdx] == stack[i] :
            idx = i
            break
    
    if idx <= len(stack) / 2 :
        while True :
            if front() == tmp[listIdx] :
                removeFirst()
                listIdx += 1
                break
            
            res += 1
            addLast(front())
            removeFirst()
    else :
        while True :
            if front() == tmp[listIdx] :
                removeFirst()
                listIdx += 1
                break
            
            res += 1
            addFirst(back())
            removeLast()
    if listIdx == m :
        break

print(res)