lis = []
while True:
    jumo = input("Enter a number: ")
    try:
        float(jumo)
        lis.append(jumo)
    except ValueError:
        if jumo.lower() == "done":
            print(f"Maximum number:  {max(lis)}\nMinimum number:  {min(lis)}")
            break
        else:
            print("wrong input please")
