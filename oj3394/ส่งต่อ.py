"""3394"""
n, s = map(int, input().split())

friend = []

for _ in range(n):
    friend.append(int(input()))

visit = set()
current = s
while current and current not in visit:
    visit.add(current)
    current = friend[current - 1]
print(len(visit))
