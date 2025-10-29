

def lg_flr(n):

	r = 0
	while n > 0:
		n >>= 1
		r += 1
	return r


# call m = lg_flr(x) and n = lg_flr(y) externally
def add(x, y, m, n):

	s = 0
	mask = 1
	cprev = 0
	msb = 1 << max(m, n)
	while mask <= msb:
		xi = x & mask
		yi = y & mask
		cnext = ((xi & yi) | (xi & cprev) | (yi & cprev)) << 1
		di = xi ^ yi ^ cprev
		s |= di
		cprev = cnext
		mask <<= 1
	return s | cnext


# call m = 1 + 2*lg_flr(x) and n = 1 + 2*lg_flr(y) externally
def mult(x, y, m, n):
	s = 0
	i = 0
	imask = 1
	for i in range(m):
		t = 0
		jmask = 1
		for j in range(n):
			xi = (x & imask) >> i
			yj = (y & jmask) >> j
			t |= ((xi & yj) << i) << j
			jmask <<= 1
		s = add(s, t, m, n)
		imask <<= 1
	return s




