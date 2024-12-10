def main():
    line = input("Enter a string: ")
    faces(line)

def faces(string):
    string = string.replace(":)", "🙂").replace(":(", "🙁")
    print(string)

main()