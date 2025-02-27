alp = str(input())
list = ["apple","banana","grape","blueberry","orange"]
cnt = 0
for i in list:
    if i[2] == alp or i[3] == alp:
        print(i)
        cnt += 1
print(cnt)