def main():
    """
        Main function of the program, where test will be made
        and errors handled
    """
    print(filter.__doc__)


def ft_filter(func, iter):
    """
        function that works like the filter() built-in function,
        take a function and an iterable as parameters
        and it will return an iterator pointing pointing to a new iterable
        containing all the element for which the function return True
        if passed to it. If no function is passed as an argument
        does the same for alle elements that are true.
    """
    if func:
        return (elem for elem in iter if func(elem))
    return (elem for elem in iter if elem)


"""
def ft_filter(func, iterable):
    ret = []
    if func:
        for elem in iterable:
            if func(elem):
                ret.append(elem)
        return iter(ret)
    for elem in iterable:
        if elem:
            ret.append(elem)
    return iter(ret)
"""


"""
def ft_filter(func, iterable):
    if func:
        for elem in iterable:
            if func(elem):
                yield elem
    else:
        for elem in iterable:
            if elem:
                yield elem
"""

if __name__ == "__main__":
    main()
