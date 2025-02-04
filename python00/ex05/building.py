import sys


def main():
    """
        Main function of the program, where test will be made
        and errors handled
    """
    try:
        if len(sys.argv) < 2:
            str = input("I need more info :\n")
        else:
            str = sys.argv[1]
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        stringInfo(str)

    except AssertionError as e:
        print(AssertionError.__name__ + ":", e, file=sys.stderr)


def unprintNum(str) -> int:
    """count the number of unprintable characters in the string"""
    count = 0
    for letter in str:
        if letter.isprintable() is False:
            count += 1
    return count


def upperNum(str) -> int:
    """count the number of upper case letters in the string"""
    count = 0
    for letter in str:
        if letter.isupper() is True:
            count += 1
    return count


def lowerNum(str) -> int:
    """count the number of lower case letters in the string"""
    count = 0
    for letter in str:
        if letter.islower():
            count += 1
    return count


def punctNum(str) -> int:
    """count the number of punctuation marks in the string"""
    count = 0
    for letter in str:
        if letter.isalnum() is False | letter.isspace() is False:
            count += 1
            print(letter)
    return count


def spacesNum(str) -> int:
    """count the number of spaces in the string"""
    count = 0
    for letter in str:
        if letter.isspace():
            count += 1
    return count


def digitsNum(str) -> int:
    """count the number of digits in the string"""
    count = 0
    for letter in str:
        if letter.isdigit():
            count += 1
    return count


def stringInfo(str):
    """
        store the number of each elements of the string in order
        to display it in the stdout
    """
    unprint = unprintNum(str)
    char = len(str) - unprint
    upper = upperNum(str)
    lower = lowerNum(str)
    punct = punctNum(str)
    spaces = spacesNum(str) - unprint
    digits = digitsNum(str)

    print(f"The text contains {char} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    main()
