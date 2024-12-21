def main():
    time = input("What time is it? ").strip()
    decimal = convert(time)

    if 7 <= decimal <= 8:
        print("breakfast time")
    elif 12 <= decimal <= 13:
        print("lunch time")
    elif 18 <= decimal <= 19:
        print("dinner time")
    else:
        return None

def convert(time):
    ans1 = time.split(":")
    hour = int(ans1[0])
    minute = int(ans1[1])

    decimal = hour + minute / 60
    return decimal

if __name__ == "__main__":
    main()

#check50 cs50/problems/2022/python/meal
#submit50 cs50/problems/2022/python/meal