stack = []

def push(n) :
    stack.append(n)
    
def pop() :
    stack.pop()
    
def isEmpty() :
    if len(stack) > 0 :
        return False
    else :
        return True
    
iron = input()
length = len(iron)
res = 0

for i in range(length) :
    if isEmpty() == True :
        push(1)
        res += 1
    else :
        if iron[i] == '(' :
            push(1)
            res += 1
        elif iron[i-1] == '(' and iron[i] == ')' :
            res -= 1
            pop()
            res += len(stack)
        elif iron[i-1] == ')' and iron[i] == ')' :
            pop()

print(res)
