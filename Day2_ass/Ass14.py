#.Program to Find Sum of Digits of a Number using Recursion.
num=(int(input("Enter a number: ")))
def sum_digits(num):
    sum=0
    while num>0:
        rem=num%10
        sum+=rem
        num=num//10
    return sum
    
result=sum_digits(num)
print("sum:",result)
