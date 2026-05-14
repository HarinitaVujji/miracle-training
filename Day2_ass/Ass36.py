#Program to Find the Sum of the Series 1/1+1/2+1/3+…1/N.
num=int(input("Enter a number:"))
sum=0
for i in range(1,num+1):
    sum=sum+(1/i)
print(sum)