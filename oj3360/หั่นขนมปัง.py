"""3360"""
w, h, _, _ = map(int, input().split())

m = list(map(int, input().split()))
n = list(map(int, input().split()))

m = [0] + m + [w]
n = [0] + n + [h]

width = []
height = []

for i in range(len(m) - 1):
    width.append(m[i + 1] - m[i])
for i in range(len(n) - 1):
    height.append(n[i + 1] - n[i])

width.sort(reverse = True)
height.sort(reverse = True)

one = width[0] * height[0]
two = max(width[1] * height[0],
          width[0] * height[1])
print(one, two)
