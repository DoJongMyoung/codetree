strs = list(map(str,input().split()))
if len(strs[0]) > len(strs[1]):
    print(strs[0], len(strs[0]))
elif len(strs[0]) < len(strs[1]):
    print(strs[1], len(strs[1]))
else:
    print("same")