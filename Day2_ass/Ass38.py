#Program to Find the Sum of the Series 1/1^0+1/2^1+1/3^2+1/4^3+1/5^4.
num=int(input("Enter a number:"))
sum=0
power=0
for i in range(1,num+1):
    sum=sum+(1/(i**power))
    power+=1
print(sum)