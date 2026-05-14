"""
A
AB
ABC
ABCD
ABCDE
ABCDEF
"""
for i in range(1,7):
    for j in range (0,i):
        print(chr(65+j),end=" ")
    print("")