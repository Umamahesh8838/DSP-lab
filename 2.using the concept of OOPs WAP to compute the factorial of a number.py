class factorialO:
    def __init__(self,n):
        self.n=n
    def calculateFactorial(self):

        if self.n < 0 :
            return "Input should be a non-negative integer."
        elif self.n ==0 or self.n ==1:
            return 1
        else:
            result=1
            for i in range(2,n+1):
                result=result*i
            return result
    def __str__(self):
        return f"the factorial of number {self.n} is {self.calculateFactorial()}"
    

n=int(input("Enter a number:"))
fact=factorialO(n)
print(fact)