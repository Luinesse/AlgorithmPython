n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n

for i in range(n) :
    dp[i] = 1
    for k in range(i) :
        if arr[i] > arr[k] and dp[i] < dp[k] + 1 :
            dp[i] = dp[k] + 1

max = 0

for i in range(n) :
    if max < dp[i] :
        max = dp[i]

print(max)