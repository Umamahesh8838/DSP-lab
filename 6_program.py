#6.	Write a Python program that checks if a given number is prime or not using control structures and relational operators.

n=int(input("Enter a number: "))
for i in range(2,n-1):
    if(n%i==0):
        print("It is not a Prime number ")
        break
else:
    print("It is a prime number")

