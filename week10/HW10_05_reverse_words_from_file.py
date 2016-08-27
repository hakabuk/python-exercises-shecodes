file_name = 'to_reverse.txt'
reversed_file = 'reverse.txt'

with open(file_name, 'r') as original_file:
    with open(reversed_file, 'w') as output_file:
        lines = original_file.readlines()
        new_list = [line[-2::-1]+'\n' for line in lines]
        output_file.write('The reversed words are: \n')
        output_file.writelines(new_list)
        output_file.write('The original list was: \n')
        output_file.writelines(lines)