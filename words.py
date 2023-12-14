#to count words in a string without using len() and split() functions
str1 = input("Enter string: ")
count = 0
for i in str1:
    if i == ' ':
        count += 1
print(count + 1)
