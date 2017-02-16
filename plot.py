# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import csv

# Honduco's method
x_1 = []
y_1 = []
stdev_1 = []

# Euclid's method
x_2 = []
y_2 = []
stdev_2 = [] 

csv.register_dialect(
	'mydialect',
    delimiter = ',',
    quotechar = '"',
    doublequote = True,
    skipinitialspace = True,
    lineterminator = '\r\n',
    quoting = csv.QUOTE_MINIMAL
)


with open('data.csv', 'rb') as mycsvfile:
	thedata = csv.reader(mycsvfile, dialect='mydialect')
	for row in thedata:
		
		if row[0] == 'mcd1':
			x_1.append(len(row[1]))# digits number	
			y_1.append(float(row[3])) # mean
			stdev_1.append(float(row[4])) # standard deviation

		elif row[0] == 'mcd2':
			x_2.append(len(row[1]))
			y_2.append(float(row[3]))
			stdev_2.append(float(row[4]))

plt.xlabel('Numero de digitos')
plt.ylabel('Segudos de ejecucion')


plt.plot(x_1, y_1)
plt.errorbar(x_1, y_1, stdev_1, linestyle='None', marker='^')
plt.savefig("test_mcd1.png")

plt.plot(x_2, y_2)
plt.errorbar(x_2, y_2, stdev_2, linestyle='None', marker='^')
plt.savefig("test_mcd2.png")