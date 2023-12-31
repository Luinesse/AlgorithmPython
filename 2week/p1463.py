dp = [0] * 1000001

n = int(input())

# 연산은 1을 빼는연산, 2로 나누는 연산, 3으로 나누는 연산이 있음.
# 1을 빼서 1이 되면 이전값에서 1뺀거랑 같으니까 dp[i - 1] + 1
# 2로 나누어 떨어져서 1이되면 현재 i 값에서 2로 나눈 몫에서 한번 더 나누면되니까 dp[i]랑 dp[i / 2] + 1이랑 비교해서 작은거 찾음
# 3은 위랑 똑같음.

for i in range(2, n+1) :
    dp[i] = dp[i - 1] + 1
    
    if i % 2 == 0 :
        dp[i] = min(dp[i], dp[i // 2] + 1)
    if i % 3 == 0 :
        dp[i] = min(dp[i], dp[i // 3] + 1)
        
print(dp[n])