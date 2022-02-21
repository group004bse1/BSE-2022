while True:
    try:
        a = []
        while True:
           N = input("Enter number: ")
           if N == "done":
            break
           N = a.append(float(N))

    except:
            print("INVALID INPUT")
            continue
    H = max(a)
    L = min(a)

    print( H,L )
    break
