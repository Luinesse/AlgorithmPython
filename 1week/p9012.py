stack = []

def push(n) :
    stack.append(n)
    
def pop() :
    stack.pop(-1)
    
def isEmpty() :
    if len(stack) == 0 :
        return True
    else :
        return False
    
t = int(input())

for i in range(t) :
    tmp = input()
    isNo = False
    length = len(tmp)
    for k in range(length) :
        if tmp[k] == '(' :
            push(1)
        else :
            if isEmpty() == True :
                print("NO")
                isNo = True
                break
            pop()
    if isEmpty() == False :
        print("NO")
        isNo = True
    
    if isNo == False :
        print("YES")
        
    if isEmpty() == False :
        for i in range(len(stack)) :
            pop()