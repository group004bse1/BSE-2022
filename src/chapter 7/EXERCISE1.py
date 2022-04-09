file = input("Enter a file name: ")
with open(file,"r") as my_file:
    for line in my_file:
        line = line.rstrip()
        print(line.upper())
