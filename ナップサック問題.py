def knapsack(N,W,weight,value):
  #初期化
  inf=float("inf")
  dp=[[-inf for i in range(W+1)] for j in range(N+1)]
  for i in range(W+1): dp[0][i]=0

  #DP
  for i in range(N):
    for w in range(W+1):
      if weight[i]<=w: #dp[i][w-weight[i]の状態にi番目の荷物が入る可能性がある
        dp[i+1][w]=max(dp[i][w-weight[i]]+value[i], dp[i][w])
      else: #入る可能性はない
        dp[i+1][w]=dp[i][w]
  return dp[N][W]