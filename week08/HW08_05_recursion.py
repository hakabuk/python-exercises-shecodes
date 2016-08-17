#01

def multiply(a, b):
    if b == 1:
        return a
    else:
        return multiply(a,b-1) + a

#02

def exp(a, b):
    if b == 1:
        return a
    else:
        return exp(a,b-1) * a

#03

def printn(n):
    print(n)
    if n == 0: return 0
    else: return printn(n - 1)


#4
def print_down(n):
    if n >= 0:
        print_down(n - 1)
        print(n)

#5
def reversed_string(str__):
    if str__ == '':
        return str__
    return str__[-1] + reversed_string(str__[:-1])

#6
def isprime(n):
    def isprime_devisor(n, d):
        if d==1:
            return True
        else:
            return bool(n%d and isprime_devisor(n, d-1))
    return isprime_devisor(n, n-1)

#7
def fib_fn(n):
    if n == 1 or n == 0:
        return n
    return fib_fn(n-1) + fib_fn(n-2)

#print(multiply(5,2))
#print(exp(5,3))
#printn(7)
#print_down(3)
#print(reversed_string('abc'))
#print(isprime(19))
#print(fib_fn(22))