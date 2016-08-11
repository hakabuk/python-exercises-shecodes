def compare_strings(string_List):
    count = 0
    for word in string_List:
        if (len(word) >= 2) and (word[0] == word[-1]):
            count += 1
    return count

string_List = ['aba', 'xyz', 'aa', 'x', 'bbb']
print(compare_strings(string_List))

string_List = ['x', 'xy', 'xyx', 'xx', '']
print(compare_strings(string_List))