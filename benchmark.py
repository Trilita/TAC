import datetime
from statistics import mean, stdev

from mcd1 import mcd1
from mcd2 import mcd2


TEST_CASES_FILE = 'testcases.txt'
REPEAT = 10
BENCHMARKS = [mcd1, mcd2]

test_cases_data = [list(map(int, l.split())) for l in open(TEST_CASES_FILE).readlines()]
results = []

# hace un benchmarking con n=REPEAT iteraciones y calcula
# la media y desviación típica.
#
# el formato de salida es:
# método empleado, números probados, media y desviación típica
for method in BENCHMARKS:
    for prime1, prime2 in test_cases_data:
        partial_results = []

        for i in range(REPEAT):
            previous_time = datetime.datetime.now()
            #method(prime1, prime2)
            elapsed_time = (datetime.datetime.now() - previous_time).total_seconds()
            partial_results.append(elapsed_time)

        print('{}, {}, {}, {}, {}'.format(
            method.__name__,
            prime1,
            prime2,
            mean(partial_results),
            stdev(partial_results)))
    print()
