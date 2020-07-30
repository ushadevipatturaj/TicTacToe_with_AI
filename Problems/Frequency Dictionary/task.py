# put your python code here
str_input = input().split()
dict_chars = {}
for i in str_input:
    if i.lower() in dict_chars:
        dict_chars[i.lower()] = dict_chars[i.lower()] + 1
    else:
        dict_chars[i.lower()] = 1
for key, value in dict_chars.items():
    print(key, value)