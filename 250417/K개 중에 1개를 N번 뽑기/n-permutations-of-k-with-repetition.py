K, N = map(int, input().split())

# Please write your code here.
answer = []


def print_answer():
    for elem in answer:
        print(elem, end=" ")
    print()


def choose(curr_num):
    # 종료 조건
    if curr_num == N + 1:
        print_answer()
        return

    for select in range(1, K+1):
            answer.append(select)
            choose(curr_num + 1)
            answer.pop()

    return


choose(1)
