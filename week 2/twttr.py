word = input("Input: ")
vow = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
wrd = ""

for i in word:
    if i not in vow:
        wrd += i

print("Output: ", wrd)

# check50 cs50/problems/2022/python/twttr
# submit50 cs50/problems/2022/python/twttr
