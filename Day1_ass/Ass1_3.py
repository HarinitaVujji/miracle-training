"""Ask the user for two numbers and print:
Sum
Difference
Product
Division"""
two_num=list(map(int,input("Enter 2 numbers:").split()))
sum=two_num[0]+two_num[1]
diff=two_num[0]-two_num[1]
product=two_num[0]*two_num[1]
div=two_num[0]/two_num[1]
#printing the sum,diff,product,division
print("Sum:",sum)
print("Difference:",diff)
print("Product:",product)
print("Division:",div)