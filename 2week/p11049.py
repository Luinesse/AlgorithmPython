n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
    
for i in range(1, n) :
    for k in range(0, n) :
        if k + i >= n :
            break
        end = i + k
        dp[k][end] = 2**31
        for j in range(k, end) :
            dp[k][end] = min(dp[k][end], dp[k][j] + dp[j + 1][end] + arr[k][0] * arr[j][1] * arr[end][1])

print(dp[0][n-1])