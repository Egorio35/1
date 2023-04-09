import random

x = set([random.randint(-10000, 10000) for _ in range(100)])
print(sorted(x, key= lambda i: (i%3)*9999+i))
