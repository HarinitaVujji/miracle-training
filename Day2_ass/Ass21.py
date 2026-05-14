#Program to print prime numbers between m to n.
m=int(input("Enter a number from where to start:"))
n=int(input("Enter a number from where to end:"))
for i in range(m,n+1):
    if i>1:
        prime=True

        for j in range(2,i):
            if i%j==0:
                prime=False
                break
        if prime:
            print(i)