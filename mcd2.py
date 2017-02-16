import sys


def mcd2(number1, number2):
	if number1 == number2:
		return number1
	else:
		current_dividend = max(number1,number2)
		current_dividing = min(number1,number2)
		while True:
			current_remainder = current_dividend % current_dividing
			if current_remainder == 0:
			 	return current_dividing
			else:
				current_dividend = current_dividing
				current_dividing = current_remainder


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('usage: python mcd1.py <num1> <num2>')
        sys.exit(-1)

    print(mcd2(int(sys.argv[1]), int(sys.argv[2])))
