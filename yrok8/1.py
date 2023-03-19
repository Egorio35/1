import time




def f(x):
    # print(x, end=", ")
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return f(x - 1) + f(x - 2)


def f1(x):
    F = [0] * (x + 1)
    F[1] = 1
    for i in range(2, x + 1):
        F[i] = F[i - 1] + F[i - 2]
    return F[x]


start = time.time()
# print(f(36))
f1(1234)
print(time.time() - start)
