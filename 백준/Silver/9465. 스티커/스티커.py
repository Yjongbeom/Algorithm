import sys
input = sys.stdin.readline

t = int(input())
result = []

for i in range(t):
    n = int(input())
    arr = []

    for _ in range(2):
        arr.append(list(map(int, input().strip().split())))

    if n == 1:
        result.append(max(arr[0][0], arr[1][0]))
    else:
        dp = [[0] * n for _ in range(2)]
        dp[0][0] = arr[0][0]
        dp[1][0] = arr[1][0]
        dp[0][1] = arr[0][1] + arr[1][0]
        dp[1][1] = arr[1][1] + arr[0][0]

        for i in range(2, n):
            dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + arr[0][i]
            dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + arr[1][i]
        
        result.append(max(dp[0][n-1], dp[1][n-1]))

for num in result:
    print(num)