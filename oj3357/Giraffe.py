"""3357"""
n = int(input())

count = 0
h = []

for i in range(n):
    h.append(int(input()))

if n == 1:
    count += 1
else:
    if h[0] > h[1]:
        count += 1
    if h[n - 1] > h[n - 2]:
        count += 1

    for i in range(1, n - 1):
        if h[i] > h[i + 1] and h[i] > h[i - 1]:
            count += 1
print(count)
