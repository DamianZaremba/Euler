#!/usr/bin/env python
import sys

if __name__ == "__main__":
	try:
		target = int(sys.argv[1])
	except TypeError:
		print "Target must be an int"
	except IndexError:
		target = 1000

	sum = 0
	for n in range(0, target):
		if n % 3 == 0 or n % 5 == 0:
			sum += n
	print "Sum: %d" % sum
