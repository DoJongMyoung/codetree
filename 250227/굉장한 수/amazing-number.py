num = int(input())
if num % 3 == 0 and num % 2 != 0:
    print("true")
elif num % 5 == 0 and num % 2 == 0:
    print("true")
else:
    print("false")
