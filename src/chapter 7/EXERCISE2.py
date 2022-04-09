file_name = input("Enter file name: ")
file_name = (file_name + ".txt")
with open(file_name,"r") as open_file:
    count = 0
    total = 0
    for line in open_file:
        if not line.startswith("X-DSPAM-Confidence:"):
            continue
        a = line.find("0")
        number = float(line[a:])
        count += 1
        total += number

    average = total/count
    print("Average spam confidence:",average)
