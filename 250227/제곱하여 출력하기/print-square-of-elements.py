N = int(input())
number = list(map(int, input().split()))

list = [i**2 for i in number]
for i in range(N):
    print(list[i], end=" ")