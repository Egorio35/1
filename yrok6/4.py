lst = [int(x) for x in input().split()]
lst.sort()
if len(lst) % 8:
    print(lst[len(lst) // 2])
else:
    print(lst[len(lst) // 2] + lst[len(lst) // 2 - 1]) / 2
