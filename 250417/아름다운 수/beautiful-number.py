n = int(input())

# Please write your code here.
#수의 분할을 표현하시오
pretty_num = [1,2,3,4]

count = 0
pretty = []
def pretty_count():

    global count

    total = sum(pretty)

    if total == n :
        count += 1
        return
        
    elif total < n:
        for i in pretty_num:
            pretty.append(i)
            pretty_count()
            pretty.pop()

            
pretty_count()
print(count)

