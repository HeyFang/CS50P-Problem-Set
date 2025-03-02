def main():
    plate = input("Plate: ").capitalize()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    # check for length
    if not (2 <= len(s) <= 6):
        return False

    # check for first 2 char
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # no symbols
    if not s.isalnum():
        return False

    # numbers at end
    has_num = False
    for i in range(len(s)):
        if s[i].isdigit():
            if not has_num and s[i] == '0':
                return False
            has_num = True
        elif has_num:
            return False



    return True
main()

# check50 cs50/problems/2022/python/plates
# submit50 cs50/problems/2022/python/plates