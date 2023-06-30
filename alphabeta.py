str1=input("Enter the string_1\n")
vowels = set(str1)
print ("\n feeded input 1 is :")
print (vowels)
str_2=input("Enter the string_2\n")
alpha = set(str_2)
print ("\n feeded input 2 is :")
print (alpha)
print ("\n Common element are :")
print(vowels.intersection(alpha))
if vowels.issubset(alpha):
    print(True)
else:
    print(False)