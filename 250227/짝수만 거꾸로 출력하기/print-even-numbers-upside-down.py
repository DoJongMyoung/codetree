N = int(input())
numbers = list(map(int, input().split()))
even = []

for i in numbers:
    if i % 2 == 0:
        even.append(i)

for i in range(len(even)):
    print(even[len(even) - i - 1], end = " ")
        