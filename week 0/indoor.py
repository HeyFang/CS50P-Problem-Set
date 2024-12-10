#take string input
def main():
    line = input(str("enter a string: "))
    turn(line)

#turn it into lowercase
def turn(string):
    print(string.lower())


main()