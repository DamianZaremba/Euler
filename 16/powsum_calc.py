#!/usr/bin/env python
import sys
import math

if __name__ == "__main__":
	try:
		target = int(sys.argv[1])
	except TypeError:
		print "Target must be an int"
	except IndexError:
		target = 1000

	tot = int(math.pow(2, target))

	sum = 0
	for x in str(tot):
		sum += int(x)
	print "Sum: %d" % sum
