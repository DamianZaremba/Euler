#!/usr/bin/env python
import sys

if __name__ == "__main__":
	try:
		target = int(sys.argv[1])
	except TypeError:
		print "Target must be an int"
	except IndexError:
		target = 20

	i = 1
	while True:
		x = 1
		good = True
		while x < target:
			if i % x > 0:
				good = False
				break
			x += 1

		if good: break
		i += 1

	print "Nuber: %s" % i
