import random

print("Hi, PyCharm")


def braz(s):
    pr = [0, 0] + [random.randint(1, 10) for _ in range(s+2)]
    print(pr)
    stupenka = [0] * (s + 4)
    for a in range(4, s + 4):
        stupenka[a] += min(pr[a - 1], pr[a - 2])
    print(stupenka[-1])


braz(int(input()))


print("Bay, PyCharm ")
