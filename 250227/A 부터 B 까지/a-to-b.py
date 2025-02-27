A, B = map(int,input().split())
while True:
    if A > B:
        break
    elif A % 2 != 0 :
        print(A,end=" ")
        A = A * 2
    else:
        print(A,end=" ")
        A = A + 3