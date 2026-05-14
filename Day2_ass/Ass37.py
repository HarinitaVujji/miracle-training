#Program to Find the Sum of the Series 1/1+1/2^2+1/3^2+1/4^2+1/5^2.
sum=0
for i in range(1,6):
    sum=sum+(1/(i*i))
print(sum)