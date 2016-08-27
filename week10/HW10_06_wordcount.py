import sys
import re
import operator


#retrieves words from file; Returns list
def get_words_list(filename):
    file_content = open(filename, 'r')
    text = file_content.read().lower()
    file_content.close()
    text = re.sub('[^a-z\ \']+', " ", text)
    words = list(text.split())
    return words


# Puts words in dictionary with value of frequency; Returns dictionary
def create_freq_dict(filename):
    freq_dict = {}
    words = get_words_list(filename)
    for word in words:
        if word not in freq_dict:
            freq_dict[word] = 0
        freq_dict[word] += 1
    del freq_dict["'"]
    return freq_dict


# Prints the dictionary in alphabetical order
def print_words(filename):
    dict = create_freq_dict(filename)
    for k, v in sorted(dict.items()):
        print("'{0}' | Frequency: {1}  ".format(k,v))
    return


# Prints 20 top frequent words from dictionary
def print_top(filename):
    freq_dict = create_freq_dict(filename)
    for k,v in sorted(freq_dict.items(), key = operator.itemgetter(1), reverse=True)[:20]:
        print("'{0}' | Frequency: {1} ".format(k,v))
    return


# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
    choice = 0
    first = True
    while not (choice == 1 or choice == 2):
        if not first:
            print("Invalid Choice: "+choice+"\n")
            first = False
        choice = int(input("What whould you like to do?\n1 count\n2 topcount\nEnter your chioce:\n"))
        filename = input("Please insert the file path:\n")
    do_choice(choice, filename)

def do_choice(choice, filename):
    option = choice
    if option == 1:
      print_words(filename)
    elif option == 2:
      print_top(filename)
    else:
      print('unknown option: ' + option)
      sys.exit(1)

if __name__ == '__main__':
    main()
