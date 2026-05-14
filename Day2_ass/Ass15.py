#Program to print the sum of alternative digits in a given number?
num=int(input("Enter a number: "))
sum=0
while num >0:
    rem=num%10
    sum+=rem
    num=num//100

print("Sum of alternative digits in the given number:",sum)
