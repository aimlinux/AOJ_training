s = int(input())

h = s/3600
m = s % 3600 / 60
s = s % 60

print(f"{int(h)}:{int(m)}:{int(s)}")