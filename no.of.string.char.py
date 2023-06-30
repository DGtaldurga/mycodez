Strng_sample="google.com"
all_freq={}
for i in Strng_sample:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1
print (all_freq)


list_char="google.com"
for i in list_char:
    print(i)