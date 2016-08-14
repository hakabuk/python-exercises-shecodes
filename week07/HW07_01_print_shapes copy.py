def triangle(t_height = 4):
    for i in range(1, t_height + 1):
        print('*'*i)
    return

def trapezoid(z_height = 4, min_width = 3):
    for i in range(1, z_height + 1):
        print('*'*i*min_width)
    return

def diamond(d_width = 8):
    for i in range(d_width - 1):
        print('{}{}'.format(' '* (d_width - i), '*'* (2*i+1)))
    for i in range(d_width - 1, -1, -1):
        print('{}{}'.format(' '* (d_width - i), '*'* (2*i+1)))
    return

t_height = int(input('Enter how tall do you want the triangle to be? '))
triangle(t_height)

z_height = int(input('How tall do you want the trapezoid to be? '))
z_width = int(input('How wide do you want the shortest line of the trapezoid to be? '))
trapezoid(z_height, z_width)

d_width = int(input('How wide do you want the diamond to be? '))
diamond(d_width)