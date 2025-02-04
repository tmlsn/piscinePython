import sys

def evenOrOdd(num : int) :
    if (num % 2) != 0 :
        print("I'm Odd.")
    else :
        print("I'm Even.")

try:
    if len(sys.argv) < 2 :
        raise AssertionError("You need to give one argument")
    if len(sys.argv) != 2 :
        raise AssertionError("more than one argument is provided")
    try:
        num = int(sys.argv[1])
    except:
        raise AssertionError("argument is not an integer")
    evenOrOdd(num)
    
except AssertionError as e:
    print(AssertionError.__name__ + ":", e, file=sys.stderr)