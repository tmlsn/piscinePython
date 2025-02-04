from ft_filter import ft_filter

def isEven(num):
    if num % 2 == 0:
        return True
    else:
        return False

test = [4, 5, 18, 12, 34, 2, 7]

ret = filter(isEven, test)

retelem = list(ret)
print(ret)

ft_ret = ft_filter(isEven, test)
print(ft_ret)

print("c good") if ret == ft_ret else print("c baaaaaaad")

ft_retelem = list(ft_ret)

print(f"normal : {retelem}")

print(f"ft : {ft_retelem}")
