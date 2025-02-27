num = list(map(int, input().split()))

min = num[0]
max = num[0]

for i in range(len(num)):
    if num[i] != 999 and num[i] != -999 and num[i] <= min:
        min = num[i]
    elif num[i] != 999 and num[i] != -999 and num[i] >= max:
        max = num[i]

print(max, min)
