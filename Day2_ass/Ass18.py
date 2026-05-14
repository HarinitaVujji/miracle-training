#Program to add the first and last digit of a given number?
num=int(input("Enter a number:"))
sum=0
last=num%10
first= num
while first>=10:
    first=first//10

sum=first+last
print("sum : ",sum)


