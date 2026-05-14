"""
ABCDEFG
ABCDEF
ABCDE
ABCD
ABC
AB
A
"""
for i in range(7,0,-1):
    for j in range(i):
        print(chr(65+j),end=" ")
    print("")