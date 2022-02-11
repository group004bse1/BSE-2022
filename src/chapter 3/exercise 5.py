w=int(input("How many guests? "))
if w <= 50:
    print("$4,000")
else:
    if w <= 100:
        print("$10,000")
    else:
        if w <= 200:
            print("$15,000")
        else:
            if w > 200:
                print("$20,000")