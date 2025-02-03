ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
print("\n")

ft_list[1] = "World!"
tup_dup = list(ft_tuple)
tup_dup[1] = "France!"
ft_tuple = tuple(tup_dup)
ft_set.discard("tutu!")
ft_set.add("Paris!")
ft_dict.update({"Hello" : "42 Paris!"})

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)