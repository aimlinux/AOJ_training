while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    if a > b:
        t = a
        a = b
        b = t
    elif a < b:
        pass
    print("{} {}".format(a, b))
