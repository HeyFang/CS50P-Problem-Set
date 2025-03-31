def main():
    s = to_percent("Fraction: ")
    if s >= 99:
        print("F")
    elif s <= 1:
        print("E")
    else:
        print(f"{s}%", end= "")

def to_percent(prompt):
    while True:
        try:
            x = input(prompt)
            x = x.split("/")
            a,b = int(x[0]), int(x[1])
            y = int(round(a/b * 100))
            if a > b:
                continue
            return y
        except (ValueError, ZeroDivisionError):
            pass

main()
