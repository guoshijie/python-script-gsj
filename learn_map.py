from collections import Iterable


def f(x):
    return x*x

def printf(list):
    if isinstance(list,Iterable):
        for i in list:
            print i

# printf(map(f,range(10)))
# printf(map(str,range(10)))

# ['adam', 'LISA', 'barT']
L = ['adam', 'LISA', 'barT']
def format(name):
    return name.capitalize()
printf(map(format,L))


