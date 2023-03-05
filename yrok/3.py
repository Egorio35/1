def fact(x: int)-> int:
    if x == 1:
        return 1
    return fact(x-1)*x


number = int(input())