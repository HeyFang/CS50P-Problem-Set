groc = {}

def main():
    grocery()

def grocery():
    while True:
        try:
            item = input().upper()
            if item not in groc:
                groc[item] = 1
            else:
                groc[item] += 1
        except EOFError:
            break
    for i in sorted(groc):
        print(f"{groc[i]} {i}")


main()
