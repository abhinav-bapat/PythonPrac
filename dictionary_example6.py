"""
Generate the following dictionary with for loop using range() function:
{2:4, 3:9, 4:16, 5:25, 6:36, 7:49, 8:64, 9:81}

"""
result = {}
for x in range(2, 10):
    result[x] = x**2

print(result)




