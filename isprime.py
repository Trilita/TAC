import sys
import datetime


def is_prime(number):
    if number == 0 or number == 1:
        return False

    for i in range(2, number):
        if number%i == 0:
            return False

    return True

def check():
    import sympy

    for i in range(0, 10*1000):
        if sympy.isprime(i) != is_prime(i):
            print("don't match")
            print(i)
            sys.exit(-1)

def benchmark(number_list):
    # http://stackoverflow.com/questions/1205722/how-do-i-get-monotonic-time-durations-in-python/14416514#14416514
    file = open('is_prime.txt', 'w+')
    for i in number_list:
        previous_time = datetime.datetime.now()
        is_a_prime = is_prime(i)
        time = datetime.datetime.now() - previous_time
        file.write("{}\t{}\t{}\n".format(i, is_a_prime, time.microseconds/1e6))


if __name__ == '__main__':
    is_prime(999999999989)
    #benchmark(range(2, 10*1000))
