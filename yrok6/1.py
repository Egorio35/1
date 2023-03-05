x, y = input().split()
if not x.isalpha() and not y.isalpha():
    if x == y:
        print("Формируем массив")
        lst = [["☻"] * int(x) for i in range(int(x))]
        for i in range(int(x)):
            for j in range(int(y)):
                if j > i:
                    lst[i][j] = "☺"
                elif i>j:
                    lst[i][j] = "🤔"

        for i in lst:
            print(" ".join(i))
