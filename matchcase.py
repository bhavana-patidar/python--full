# x = int(input("Emter the value of x:"))
# match x:
#     case 0:
#         print("x is zero")
#     case 4:
#         print("x % 2==0 and case is 4")
#     case _:
#         print(x)


#with ifelse
x = int(input("Emter the value of x:"))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
    case _ if x!=90:
        print(x,"is not 90")
    case _ if x!=80:
        print(x, "is not 80")
    case _:
        print(x)

