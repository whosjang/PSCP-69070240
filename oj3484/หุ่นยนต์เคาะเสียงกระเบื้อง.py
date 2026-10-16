"""หุ่นยนต์เคาะเสียงกระเบื้อง"""
n, p = map(int, input().split())

grid = []
for i in range(n):
    row = list(map(int, input().split()))
    grid.append(row)

row_broken = [0] * n
row_point = [0] * n
col_broken = [0] * n
col_point = [0] * n
total_broken = 0
total_point = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] > 0:
            row_broken[i] += 1
        row_point[i] += grid[i][j]
        col_point[j] += grid[i][j]
for j in range(n):
    for i in range(n):
        if grid[i][j] > 0:
            col_broken[j] += 1
for i in range(n):
    total_broken += row_broken[i]
    total_point += row_point[i]
for i in range(n):
    print(f"{' '.join(map(str, grid[i]))} {row_broken[i]} {row_point[i]}")

print(' '.join(map(str, col_broken)))
print(' '.join(map(str, col_point)))
print(f"{total_broken} {total_point} {total_point * p:.2f}")
