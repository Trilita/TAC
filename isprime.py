import sys
import datetime


def is_prime(number):
    if number == 0 or number == 1:
        return False

    for i in range(2, number):
        if number%i == 0:
            return False

    return True

def is_prime_v1(number):
    if number == 0 or number == 1:
        return False

    if number == 2:
        return True

    if number % 2 == 0:
        return False

    i = 3
    while i < number-1:
        if number%i == 0:
            return False
        i += 2

    return True

# comprueba que nuestra implementación es correcta
# usando la librería de cálculo simbólico `sympy`
# y contrastando ambos resultados
def check(function, until=10*1000):
    import sympy

    for i in range(0, until):
        if sympy.isprime(i) != function(i):
            print("doesn't match")
            print(i, sympy.isprime(i), function(i))
            sys.exit(-1)

    print('everything ok :)')

if __name__ == '__main__':
    methods = [is_prime, is_prime_v1]
    for method in methods:
        print('checking {}'.format(method.__name__))
        check(method)

    #if len(sys.argv) < 2:
    #    print('usage: python isprime.py <number>')
    #    sys.exit(-1)
    #print(is_prime(int(sys.argv[1])))
