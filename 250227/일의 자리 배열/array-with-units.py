number = list(map(int, input().split()))

for i in range(8):
    number.append((number[i] + number[i + 1]) % 10)
for i in number:
    print(i,end=" ")