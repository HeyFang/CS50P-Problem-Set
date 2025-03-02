word = input("camelCase: ")

b = word[0].lower()
for i in range(1, len(word)):
    if word[i].isupper():
        b += "_"
    b += word[i].lower()

print("snake_case:", b)

# check50 cs50/problems/2022/python/camel
# submit50 cs50/problems/2022/python/camel