b=int(input("what is your age? "))
if b >= 18:
    print("you can vote.")
elif b > 0 and b <= 17:
    print("too young to vote")
elif b < 0:
    print("you are a time traveller")