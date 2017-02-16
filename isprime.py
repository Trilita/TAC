import sys
import datetime


def is_prime(number):
    if number == 0 or number == 1:
        return False

    for i in range(2, number):
        if number%i == 0:
            return False

    return True

# comprueba que nuestra implementación es correcta
# usando la librería de cálculo simbólico `sympy`
# y contrastando ambos resultados
def check(until=100):
    import sympy

    for i in range(0, until):
        if sympy.isprime(i) != is_prime(i):
            print("don't match")
            print(i)
            sys.exit(-1)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('usage: python isprime.py <number>')
        sys.exit(-1)
    print(is_prime(int(sys.argv[1])))
