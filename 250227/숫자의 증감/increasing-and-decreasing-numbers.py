C , N = map(str, input().split())
num = int(N)
if C == "A":
    for i in range(1, num+1):
        print(i, end=" ")
elif C =="D":
    for i in range(num,0,-1):
        print(i, end=" ")
