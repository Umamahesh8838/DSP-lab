# n=input("Enter Expression: ")
# print("Ans:",eval(n))

print("Uma Maheswara Reddy M\n1/22/FET/BCS/358")


while(True):
    x=input("Enter Operator :(*,+,-,/,%) [0 to exit] ")
    if x=='0':
        print("Bye")
        break
    n1=int(input("Enter Number 1: "))
    n2=int(input("Enter Number 2: "))
    if x=='*':
        print("ans: ",n1*n2)
    elif x=='+':
        print('ans: ',n1+n2)
    elif x=='-':
        print('ans: ',n1-n2)
    elif x=='/':
        print('ans: ',n1/n2)
    elif x=='%':
        print('ans: ',n1%n2)
    else:
        print("Invalid operator")
    print(20*"-")

