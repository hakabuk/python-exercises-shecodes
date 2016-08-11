def cipher(my_string, shift = 13):
    message = ''
    for i in range(len(my_string)):
        char = my_string[i]
        if char == ' ':
            message += char
        elif char.isalpha():
            asciiValue = ord(char) + shift
            if (asciiValue > 90):
                asciiValue -= 26
            message += chr(asciiValue)
        else:
            break
    #Check if the process was completed
    if len(my_string) != len(message):
        return 'Could not complete action - there was a problem with your original message'
    return message

# cipher works for capital letters only
my_string = 'THIS LV QRW PB FDU'
shift = 13
print(cipher(my_string, shift))