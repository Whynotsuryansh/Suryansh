n='suryansh'
vowel= 'aeiouAEIOU'
count_v= 0
count_c=0
for i in n:
    if i in vowel:
        count_v=count_v+1
    else:
        count_c=count_c+1
print("Vowels", count_v)
print("Cons", count_c)
