ans = input("What is the answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()

correct = ["42", "forty-two", "forty two"]

if ans in correct:
    print("Yes")
else:
    print("No")
    
# check50 cs50/problems/2022/python/deep
# submit50 cs50/problems/2022/python/deep