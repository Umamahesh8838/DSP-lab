def factorialP(n):
    if n==0 or n==1 :
        return 1
    else:
        result=1
        for i in range(2,n+1):
            result*=i
        return result
n=int(input("enter a number:"))
print("factorial of",n,"is",factorialP(n))
