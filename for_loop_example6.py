"""
Find out and print the vowels in a given word
word = 'Milliways'
vowels = ['a', 'e', 'i', 'o', 'u']
"""
word = 'Milliways'
vowels = ['a', 'e', 'i', 'o', 'u']
result=[]
for x in word:
    if x in vowels:
        if x not in result:
            result.append(x)
print(result)








