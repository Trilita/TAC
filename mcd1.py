import sys
from collections import Counter


# Algoritmo 1:
#   Descomposición de los números en sus factores primos, y multiplicación de los factores comunes con el menor exponente.
def factorize(number):
    factors = []
    primes = open('primes/all_primes.txt')
    while True:
        current_prime = int(primes.readline())
        while number % current_prime == 0:
            factors.append(current_prime)
            number /= current_prime

            if number == 1:
                return factors

def mcd1(number1, number2):
    factors_1 = Counter(factorize(number1))
    factors_2 = Counter(factorize(number2))

    intersection = (factors_1 & factors_2)
    result = 1
    for k, v in intersection.items():
        result *= k ** v

    return result


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage: python mcd1.py <num1> <num2>')
        sys.exit(-1)

    #print(factorize(int(sys.argv[1])))
    print(mcd1(int(sys.argv[1]), int(sys.argv[2])))

