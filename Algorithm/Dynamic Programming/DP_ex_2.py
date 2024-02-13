'''
N×N 행렬이 주어졌을 때, (1,N)에서 시작하여 왼쪽 혹은 밑으로만 이동하여 (N,1)로 간다고 했을 때 
거쳐간 위치에 적혀있는 숫자의 합을 최소로 하는 프로그램을 작성해보세요.
'''
N = int(input())

data = [list(map(int,input().split())) for _ in range(N)]

dp_table = [[0 for _ in range(N)] for _ in range(N)]

# 초기값 설정
dp_table[0][N-1] = data[0][N-1]

# init table make
for i in range(N-2,-1,-1):
    dp_table[0][i] = dp_table[0][i+1] + data[0][i]
    
for i in range(1,N):
    dp_table[i][N-1] = dp_table[i-1][N-1] + data[i][N-1]

# i , j 기준 위 (i-1,j) 왼쪽,(i,j+1) 비교해서 작은거
# dp_table[i][j] = min(dp_table[i-1],[j],dp_table[i][j+1]) + data[i][j]
for j in range(N-2,-1,-1):
    for i in range(1,N):
        dp_table[i][j] = min(dp_table[i-1][j],dp_table[i][j+1]) + data[i][j]

# i,j
# for i in range(N-2,-1,-1):
#     for j in range(1,N):
#         dp_table[j][i] = min(dp_table[j-1][i]+data[j][i],dp_table[j][i-1]+data[j][i])

print(dp_table[-1][0])
