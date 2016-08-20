#01

movies = ['The notebook', 'Black Swan', 'War of the worlds']
actress = ['Rachel McAdams', 'Natalie Portman', 'Dakota Fanning']

my_dict = dict(zip(actress, movies))
my_list = [k + ' stars in ' + s for (k,s) in my_dict.items()]

#02
my_list = [i*100 if i%2 == 0 else i for i in range(1,10) ]

#03
my_list = [i*100 for i in range(1,10) if i%2 == 0 ]

#04
my_list = ['Boom' if i%7 == 0 else i for i in range(1,100)]


print(my_list)