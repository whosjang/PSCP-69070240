"""3017"""
def main():
    """bill"""
    cash = int(input())

    if 500 <= cash <= 10000:
        charge = cash * 0.1
        vat = cash * 0.07
        bill = cash + charge + vat
        print(f"{bill:.02f}")
    elif 500 < cash > 10000:
        vat = cash * 0.07
        bill = cash + vat
        print(f"{bill:.02f}")
main()
