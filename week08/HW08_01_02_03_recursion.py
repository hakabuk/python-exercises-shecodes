#01

def sum(n):
    if n == 1:
        return 1

    return sum( n-1 ) + n

#02

def sum_every_other_number(n):
    if n in (0,1): return n

    return sum_every_other_number(n-2) + n


def fibonacci(n):
    if n in(0,1): return n

    return fibonacci(n-1) + fibonacci(n-2)

#03

def hailstone(n):
    print(n)
    if n == 1: return 1
    elif n%2 == 0:
        return 1 + hailstone(n//2)
    else: return 1 + hailstone(n*3+1)


print(sum( 5 ))
print(sum_every_other_number(10))
print(fibonacci(12))
hailstone(10)
