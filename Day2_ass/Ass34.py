#Program to print Odd and Even Numbers from an Array.
arr=[17,24,30,43,55,60]
even_sum=0
odd_sum=0
for i in arr:
    if i%2==0:
        even_sum+=i
    else:
        odd_sum+=i
print("Even sum of elements in array:",even_sum)
print("Odd sum of elements in array:",odd_sum)