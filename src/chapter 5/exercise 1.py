total=0
v=0
while True:
    number=input('enter number :').lower()
    try:
        if number == "done":
            print(v, total,total/v )
            break
        int(number)
    except:
        print('invalid')
        continue
    number=int(number)
    v +=1
    total = total + number

