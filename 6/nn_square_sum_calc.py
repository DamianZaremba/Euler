#!/usr/bin/env python
import sys
import math

if __name__ == "__main__":
	try:
		target = int(sys.argv[1])
	except TypeError:
		print "Target must be an int"
	except IndexError:
		target = 100

	square_sum = 0
	for x in range(1, target+1):
		square_sum += math.pow(x, 2)

	sum = 0
	for x in range(1, target+1):
		sum += x
	sum_square = math.pow(sum, 2)

	difference = sum_square - square_sum
	print "Difference: %d" % difference
