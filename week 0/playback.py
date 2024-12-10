def main():
    #take input string
    line = input(str("Enter a string: "))
    playback(line)

def playback(string):
    string = string.replace(" ", "...")
    print(string)

main()