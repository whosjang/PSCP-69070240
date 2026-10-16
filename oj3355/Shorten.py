"""3355"""
n = int(input())

start = n
last = n
ans = []

while n != -1:
    n = int(input())
    if n == -1:
        if start == last:
            ans.append(str(start))
        else:
            ans.append(f"{start}-{last}")
        break

    if n == last + 1:
        last = n
    else:
        if start == last:
            ans.append(str(start))
        else:
            ans.append(f"{start}-{last}")
        start = n
        last = n
print(", ".join(ans))
