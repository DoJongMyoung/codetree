n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j == n:  # 마지막 요소인 경우
            print(f"{i} * {j} = {i * j}", end="")  # 끝에 , 없음
        else:
            print(f"{i} * {j} = {i * j}", end=", ")  # 끝에 , 추가
    print()  # 줄 바꿈
