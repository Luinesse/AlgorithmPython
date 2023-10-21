n,k = map(int, input().split())

coin = [0] * n

for i in range(n) :
    coin[i] = int(input())

dp = [0] * 10001
dp[0] = 1

for i in range(n) :
    for j in range(coin[i], k + 1) :
        dp[j] += dp[j - coin[i]]

print(dp[k])