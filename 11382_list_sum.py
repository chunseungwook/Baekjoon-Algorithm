value_in = input()
list_value = value_in.split(" ")
list_value_int = list(map(int, list_value))
result = sum(list_value_int)
print(result)