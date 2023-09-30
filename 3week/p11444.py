mod = 1000000007

def multiply(a, b, res) :
    for i in range(2) :
        for k in range(2) :
            tmp = 0
            for l in range(2) :
                tmp += a[i][l] * b[l][k]
            res[i][k] = tmp % mod

def copyArr(a, b) :
    for i in range(2) :
        for k in range(2) :
            b[i][k] = a[i][k]

def conq(a, tmp, res, n) :
    if n == 1 :
        copyArr(a, res)
        return
    conq(a, tmp, res, n // 2)

    copyArr(res, tmp)
    multiply(tmp, tmp, res)

    if n % 2 == 1 :
        copyArr(res, tmp)
        multiply(tmp, a, res)
    copyArr(res, tmp)

n = int(input())
a = [[1,1],[1,0]]
tmp = [[1,1],[1,1]]
res = [[1,1],[1,1]]

conq(a,tmp,res,n)

print(res[0][1])