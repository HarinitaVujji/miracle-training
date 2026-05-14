#16.Program to print the no of occurrences of a digit in a number.
num=int(input("Enter a number:"))
digit= int(input("Enter the digit from the number for count: "))
occ=0
while num >0:
    rem=num%10
    if rem==digit:
        occ+=1
    num=num//10
print(occ)
    