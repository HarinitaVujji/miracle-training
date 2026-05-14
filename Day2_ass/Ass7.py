#Print sum of all even numbers b/w 1 to n.
n= int(input("Enter number:"))
sum=0
for i in range (2,n+1,2):
    sum+=i

print(sum)