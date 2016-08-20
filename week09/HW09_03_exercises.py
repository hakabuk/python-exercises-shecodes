#01

def create_dict(my_string):
    my_dict = {}
    for i in range(len(my_string)):
        char = my_string[i].lower()
        if char.isalpha():
            if (char in my_dict):
                my_dict[char] += 1
            else:
                my_dict[char] = 1
        else:
            continue
    return my_dict

def anagram(t,s):
    return create_dict(t) == create_dict(s)


t = 'aba'
s = 'baa'
print(anagram(t,s))

#02

#creates a dictionary with number of each wanted character: 'MDCLXVI'
def create_dict(roman_number, char_str):
    my_dict = {}
    for i in range(len(roman_number)):
        upper_roman = roman_number.upper()
        char = upper_roman[i]
        if char.isalpha() and char in upper_roman:
            if (char in my_dict):
                my_dict[char] += 1
            else:
                my_dict[char] = 1
        else:
            continue
    return my_dict

def convert_numeric(count_dict):
    value_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    value = [v*(value_dict[k]) for (k,v) in count_dict.items()]
    return sum(value)

char_str = 'MDCLXVI'
roman_number = 'DcXXI'
count_dict = create_dict(roman_number, char_str)
print(convert_numeric(count_dict))

#03:

def plus_one(my_list):
    enumerated = [s*(10**(len(my_list)-i-1)) for (i,s) in enumerate(my_list)]
    return [int(i) for i in str(sum(enumerated) + 1)]


my_list = [5, 6, 3]
print(plus_one(my_list))