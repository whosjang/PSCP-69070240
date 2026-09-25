"""3296"""
R1, G1, B1 = map(int, input().split())
R2, G2, B2 = map(int, input().split())

red = (R1 + R2) // 2
green = (G1 + G2) // 2
blue = (B1 + B2) // 2

print(f"{red} {green} {blue}")
