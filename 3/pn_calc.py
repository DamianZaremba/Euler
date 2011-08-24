#!/usr/bin/env python
import sys

if __name__ == "__main__":
	try:
		target = int(sys.argv[1])
	except TypeError:
		print "Target must be an int"
	except IndexError:
		target = 600851475143

	i = 2
	prime = 0
	while i <= target:
		if target % i == 0:
			prime = i

			target = target / i;
			i -= 1

			if target == 1:
				break
		i += 1
	print "Largest prime factor found: %d" % prime
