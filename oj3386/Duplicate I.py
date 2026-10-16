m = int(input())
n = int(input())

m_list = []
n_list = []

for _ in range(m):
    num = int(input())
    m_list.append(num)
for _ in range(n):
    num = int(input())
    n_list.append(num)

shown = []
for num in m_list:
    if num in n_list and num not in shown:
        shown.append(num)

shown.sort(reverse=True)
if shown:
    for num in shown:
        print(num)
else:
    print("Nope")
