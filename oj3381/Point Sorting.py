"""3381"""
t = int(input())

for _ in range(t):
    n = int(input())
    point = []
    for _ in range(n):
        x, y = map(int, input().split())
        point.append((x, y))
    point.sort(key=lambda p: (p[0] + p[1], -p[1]))
    for x, y in point:
        print(x, y)
