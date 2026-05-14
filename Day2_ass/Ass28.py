#.Program to find the frequency of each element in the array.
arr = [1, 2, 2, 3, 4, 3, 2, 1]

visited = []

for i in arr:

    if i not in visited:
        count = 0

        for j in arr:
            if i == j:
                count += 1

        print(i, "occurs", count, "times")

        visited.append(i)