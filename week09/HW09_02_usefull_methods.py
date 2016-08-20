#07
sum = lambda x,y: x+y
print(sum(1,5))

#08
joules = [5000, 8000, 10000, 6000, 12000]
print(list(map(lambda x: (x, x/4184.0), joules)))

#09
my_range = list(range(1,7))
print([(a, b) for a in my_range for b in my_range])
#print(len([(a, b) for a in my_range for b in my_range]))

#10
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print(list(filter(lambda x: x == "Python", languages)))