def f(x: str):
    if not x:
        return 0
    elif x[0].isalpha():
        return f(x[1:])
    elif x[0].isdigit():
         return f(x[1:]) + 1
    else:
        return f(x[1:])

text = input()
print(f(text))