#!/usr/bin/env python
import sys

if __name__ == "__main__":
	try:
		target = int(sys.argv[1])
	except TypeError:
		print "Target must be an int"
	except IndexError:
		target = 100

	i = target-1
	n = target
	while i > 0:
		n *= i
		i -= 1

	sum = 0
	for x in str(n):
		sum += int(x)
	print "Sum: %d" % sum
