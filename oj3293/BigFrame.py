"""3293"""
text = []

for i in range(5):
    text.append(input().rstrip())
max_len = 0
for i in text:
    if len(i) > max_len:
        max_len = len(i)
print("*" * (max_len + 4))

for i in text:
    print("*", i.ljust(max_len), "*")
print("*" * (max_len + 4))
