N , M = map(int,input().split())
arr = [[0 for i in range(N)] for j in range(N)]
for i in range(1,M+1):
    a , b = map(int,input().split())
    arr[a-1][b-1] = i

for i in range(N):
    for j in range(N):
        print(arr[i][j],end=" ")
    print()
