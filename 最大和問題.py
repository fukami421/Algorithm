# input
n = int(input())
a = list(map(int, input().split()))

dp =[0] # 初期値

for i in range(n):
  i_max = max(dp[i], dp[i] + a[i])
  dp.append(i_max)

print(dp[-1]) # 最後の値が最大値になっている
