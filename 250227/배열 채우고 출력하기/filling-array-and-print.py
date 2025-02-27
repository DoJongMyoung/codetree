numbers = list(map(str,input().split()))
for i in range(len(numbers)):
    print(numbers[len(numbers) - i - 1],end="")
