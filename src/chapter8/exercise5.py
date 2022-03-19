count = 0
while True:
    try:
        jumo = input("Enter the file name: ").lower()
        with open(jumo, "r") as new_file:
            for lin in new_file:
                if lin.startswith("From:"):
                    continue
                elif lin.startswith("From"):
                    var = lin.split()
                    print(var[1])
                    count += 1
        print("There were ", count, "lines in the file with From as the first word ")
        break
    except:
        print("file not found!")
