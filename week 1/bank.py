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