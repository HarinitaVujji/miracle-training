#Program to print n perfect numbers.
num=int(input("Enter a number:"))
count=0
n=1
while count<num:
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum==n:
        print(n)
        count+=1
    n+=1