n = int(input("введите кол--во учеников: "))
count = 0
count_T = 0
if 1 <= n <= 30:
    for i in range(n):
        N = int(input("введите кол--во решённых заданий: "))
        if 5 > N:
            count += 1
        if N == 10:
            count_T += 1
print(count)
if count_T > 0:
    print("YES")
elif count_T == 0:
    print("NO")

