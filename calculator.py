a=int(input("enter the first value"))
b=int(input("enter the second value"))
for i in range(5):
    print("Calculator menu")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    print("5.exit")
    choice=int(input("enter your choice"))
    if choice==1:
        c=a+b
        print("sum:",c)
    elif choice==2:
        c=a-b
        print("difference:",c)
    elif choice==3:
        c=a*b
        print("product:",c)
    elif choice==4:
        c=a/b
        print("quotient:",c)
    elif choice==5:
        break
    else:
        print("Invalid Choice")
    
