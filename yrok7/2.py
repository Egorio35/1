def s(lst):  # lst = [7, 8, 1, 0, 2]
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    print(lst)


def s2(lt, rt):
    if len(lt) == 0:
        return lt
    if len(lt) == 0:
        return lt
    resuln  = []
    index_l = index_r = 0
    while len(resuln)< len(rt) + len(lt):
        if rt[0] > lt[0]:
            resuln.append(lt[index_l])
            index_l += 1
        else:
            resuln.append(rt[index_r])
            index_r += 1


    return resuln


def merge(lst):
    lt, rt = lst[0:int(len(lst) / 2)], lst[int(len(lst) / 2):]
    print(lt)
    print(rt)
    if len (lt) >= 2:
        merge(lt)
    if len(lt) >= 2:
        merge(lt)

lst = [7, 8, 1, 0, 2, 10]

#merge(lst)
print(s2([1,2], [2, 9, 0]))