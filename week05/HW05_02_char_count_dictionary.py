def create_dict(my_string, user_string):
    my_dict = {}
    for i in range(len(my_string)):
        user_lower = user_string.lower()
        char = my_string[i].lower()
        if char.isalpha() and char in user_string:
            if (char in my_dict):
                my_dict[char] += 1
            else:
                my_dict[char] = 1
        else:
            continue
    return my_dict


my_string = 'ack55YYtge6be56n7e5ybc'
user_string = 'kkk'
print(create_dict(my_string, user_string))