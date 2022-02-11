a=int(input("how many hours? "))
try:
    b=float(input('what is rate? '))
    if a > 40 :
        print(((((a-40)*15/10)*b)+40*b))
    else:
        print(a*b)
except:
    print("error,please enter numeric input ")