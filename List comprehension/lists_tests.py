# Examples
numbers = [1, 2, 3]
# To remember it is like that
# new_numbers = [new_item for item in list]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

# Goes through each letter and puts it separately into a list
name = "Angela"
new_name = [letter for letter in name]
print(new_name)


new_range_list = [n * 2 for n in range(1, 5)]
print(new_range_list)

names = ["Angela", "Vlad", "Alvaro"]
uppercase_names = [name.upper() for name in names if len(name) > 5]
print(uppercase_names)
