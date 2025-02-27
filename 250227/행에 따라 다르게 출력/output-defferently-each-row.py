n = int(input())
cnt = 0
for i in range(n):
    num = []
    if i % 2 == 0 : #홀수줄인 경우
        for j in range(1,n+1):
            cnt += 1
            num.append(cnt)
    if i % 2 == 1 : #짝수줄인 경우
        for j in range(1,n+1):
            cnt += 2
            num.append(cnt)

    for k in range(n):
        print(num[k],end=" ")
    print()