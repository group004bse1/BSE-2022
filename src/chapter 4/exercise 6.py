def compute_pay():
    a = int(input("enter hours:"))
    b = float(input("enter rate:"))
    if a > 40:
        print(((((a - 40) * 15 / 10) * b) + 40 * b))
    else:
        print(a * b)


compute_pay()
