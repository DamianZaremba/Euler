#!/usr/bin/env python
import sys

if __name__ == "__main__":
	try:
		target = int(sys.argv[1])
	except TypeError:
		print "Target must be an int"
	except IndexError:
		target = 4000000

	sequence = [1, 2]
	while True:
		p1 = sequence[-1]
		p2 = sequence[-2]
		step = p2+p1

		if step >= target:
			break

		sequence.append(step)

	sum = 0
	for item in sequence:
		if item % 2 == 0:
			sum += item
	print "Sum: %d" % sum
