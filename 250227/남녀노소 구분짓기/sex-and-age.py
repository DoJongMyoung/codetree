gender = int(input())
age = int(input())
if gender == 0:
    if age >= 19:
        print("MAN")
    else:
        print("Boy")
else:
    if age >= 19:
        print("WoMAN")
    else:
        print("GIRL")       