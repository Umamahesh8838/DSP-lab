print("UMA MAHESWAR REDDY MOLAKALA\n1/22/FET/BCS/358")
a=[2,3,4,5,6,7]


def func_sum(a):
    n=len(a)+1
    actual_sum=n*(n+1)/2
    print("using sum method:",int(actual_sum-sum(a)))


def func(a):
    for x in range(1,max(a)+1):
        if(x not in a):
            print(x,end=" ")
func_sum(a)
func(a)
