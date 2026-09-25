"""3299"""
L, N = map(int, input().split())

last = 1

while last * L * (last * L + 1) // 2 < N:
    last += 1
print(last)
