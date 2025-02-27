num = int(input())

while True:
    if num == 25:
        print("Good")
        break
    elif num > 25:
        print("Lower")
    else:
        print("Higher")
    num = int(input())
