file_name = 'to_reverse.txt'

with open(file_name, 'r') as reading_file:
    for line in reading_file.readlines():
        print(line)

'''

#Write will empty the file if it's there already
#or create it
example_file = open(file_name, 'w')

try:
    example_file.write("Blue goose on the loose\n")
    example_file.write("Honeycomb cereal\n")

except Exception as error:
    print("Problem handling file, eror was %s" % error)

finally:
    example_file.close()

#it's better to use "with... open .... as - the file gets closed for me
with open(file_name, 'w') as example_file:
    #this is where example_file 'lives'. it does not exist after this
    lines = ["Happy whale on parade\n",
             "Red bee dancing\n",
             "Great gig in the sky\n"]
    #pass in a list and write lines does iteration
    example_file.writelines(lines)

#reading the file
with open(file_name, 'r') as reading_file:
    for line in reading_file.readlines():
        print(line)


#another way of reding a file:
with open(file_name, 'r') as reading_file:
    text = reading_file.read()
    print(text)


#make every second letter uppercase and the others lowercase:
#read file --> manipulate content --> write back to file
new_content = []
file_content = ''
counter = 0

with open(file_name, 'r') as reading_file:
    file_content = reading_file.read()

for charachter in file_content:
    if counter % 2 == 0:
        new_content.append(charachter.upper())
    else:
        new_content.append(charachter.lower())
    counter += 1

new_content = ''.join(new_content)

with open(file_name, 'w') as writable_file:
    writable_file.write(new_content)


#another solution with 'a':
with open(file_name, 'a') as appending_file:
    for char in new_content:
        #since we're in append mode - it will not delete the file but append to it
        appending_file.write(char)

'''






