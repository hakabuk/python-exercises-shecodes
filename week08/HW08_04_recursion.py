#04
def paths(m, n):
    if m==1 or n==1:
        return 1
    return paths(m, n-1) + paths(m-1, n)



#print(paths(3, 3))