months =["January","February","March","April","May","June","July","August","September","October","November","December"]

def main():
    while True:
        try:
            date = input("Date: ").strip()

            if "/" in date:
                month, day, year = date.split("/")
                month, day, year = int(month), int(day), int(year)

                if 0 < month < 13 and 0 < day < 32:
                    print(f"{year}-{month:02}-{day:02}")
                    break

            # September 9, 1111
            elif "," in date:
                month, day, year = date.replace(",", "").split(" ")
                day, year = int(day), int(year)

                if month in months and 0 < day < 32:
                    month = months.index(month) + 1
                    print(f"{year}-{month:02}-{day:02}")
                    break
            else:
                pass
        except (ValueError, IndexError):
            pass




main()
