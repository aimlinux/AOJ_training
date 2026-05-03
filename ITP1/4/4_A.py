a, b = map(int, input().split())

# d = int(a / b)
# r = int(a % b)
# f = float(a) / float(b)

# print("{} {} {}".format(d, r, f))

d = a // b
r   = a % b
f = a / b

print(f"{d} {r} {f:0.5f}")