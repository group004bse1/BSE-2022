while True:
    file_name = input(" Enter the name of the file: ").lower()
    try:
        with open(file_name, "r") as new_file:
            pam = []
            for line in new_file:
                jumo = line.split()
                for pp in jumo:
                    if pp not in pam:
                        pam.append(pp)
        pam.sort()
        print(pam)
        break
    except:
        print("file not found!")
