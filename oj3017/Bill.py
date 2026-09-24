"""3017"""
def main():
    """bill"""
    cash = int(input())

    charge = cash * 0.1

    if charge < 50:
        charge = 50
    elif charge > 1000:
        charge = 1000

    vat = (cash + charge) * 0.07
    bill = cash + charge + vat
    print(f"{bill:.02f}")
main()
