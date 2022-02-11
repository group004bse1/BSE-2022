location_input= input("which location? ")
pay_input=int(input("enter the pay "))
if location_input=="kampala":
    if pay_input>=10000000:
        print("i will take it")
    else:
        print("no way")
elif location_input=="mbarara":
    if pay_input>4000000:
        print("i will take it")
    else:
        print("no thanks i will find something better")
elif location_input=="space":
    print("without doubt i will take it")

else:
    if pay_input>=6000000:
        print("i will take it")
    else:
        print("no thanks i will find something better")



