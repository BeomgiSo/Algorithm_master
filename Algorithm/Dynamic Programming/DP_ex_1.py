
'''
N×N 행렬이 주어졌을 때,
(1,1)에서 시작하여 오른쪽 혹은 밑으로만 이동하여 
(N,N)으로 간다고 했을 때 거쳐간 위치에 적혀있는 
숫자의 합을 최대로 하는 프로그램을 작성해보세요.
'''


N = int(input())

data = [list(map(int,input().split())) for _ in range(N)]

dp_table = [[0 for _ in range(N)] for _ in range(N)]

# [1,1] 에서 시작해서 오른쪽 혹은 밑 으로만 이동
# init -> 오른쪽으로 쭉 더한거  // 밑으로 쭉 더한거
dp_table[0][0] = data[0][0]

for i in range(1,N):
    dp_table[0][i] = data[0][i] + dp_table[0][i-1]
    
for i in range(1,N):
    dp_table[i][0] = data[i][0] + dp_table[i-1][0]

# i,j 현재 위치
# dp_table[i][j] = max(dp_table[i-1][j]+data[i][j],dp_table[i][j-1] + data[i][j])
for i in range(1,N):
    for j in range(1,N):
        dp_table[i][j] = max(dp_table[i-1][j]+data[i][j],dp_table[i][j-1] + data[i][j])
        
print(dp_table[-1][-1])

