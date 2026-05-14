#Program to take the number at runtime and check whether the given number is positive or negative.
num = int(input("Enter a number: "))
if (num>0):
    print(num,"is a positive number.")
elif (num<0):
    print(num ,"is a negative number.")
else:
    print("Zero")