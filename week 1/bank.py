greet = input("Greeting: ").lower()

fgreet = greet.split()
fword = fgreet[0]

fletter = greet[0]

if fword == "hello":
    print("$0")
elif fletter == "h":
    print("$20")
else:
    print("$100")

#check50 cs50/problems/2022/python/bank
#submit50 cs50/problems/2022/python/bank