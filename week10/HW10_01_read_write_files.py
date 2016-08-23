fw = open('sample.txt', 'w')

fw.write('This is my file\nI like avocado')
fw.close()

fr = open('sample.txt', 'r')
text = fr.read()
fr.close()

print(text)