num = []
cnt3 , cnt5 = 0, 0
for i in range(10):
    num.append(int(input()))

for i in num:
    if i % 3 == 0:
        cnt3 += 1
    if i % 5 == 0:
        cnt5 += 1

print(cnt3,cnt5)