dp = [0] * 1000001

n = int(input())
arr = list(map(int, input().split()))

dp[0] = arr[0]

for i in range(1, n) :
    if arr[i] + dp[i - 1] > arr[i] :
        dp[i] = arr[i] + dp[i - 1]
    else :
        dp[i] = arr[i]
max = dp[0]

for i in range(1, n) :
    if max < dp[i] :
        max = dp[i]
        
print(max)