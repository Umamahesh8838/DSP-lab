# n=input("Enter Expression: ")
# print("Ans:",eval(n))

n1=int(input("Enter Number 1: "))
n2=int(input("Enter Number 2: "))


x=input("Enter Operator :(*,+,-,/,%)  ")
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

