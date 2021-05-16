n=int(input("Enter number of terms :"))
a,b=0,1
i=0
if n==1:
    print(a)
else:
    for i in range(n):
        c=a+b
        print(a,end=",")
        a=b
        b=c
