def sum(x: int):
    global count
    count+=1
    if x ==0:
        return 0
    return sum(x-1) + x


count = 0
print(sum(997))
print(count)