n = int(input())
for i in range(n):
    num = []
    for j in range(1,n+1):
        num.append(j)
    if i % 2 == 1:
        num.reverse()
    for k in range(n):
        print(num[k],end="")
    print()