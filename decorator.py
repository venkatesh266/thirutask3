def check_b(f):
	def wrap(a,b):
		if b != 0:
			return f(a, b)
		else:
			return 'b should not be Zero'
	return wrap


def div(a, b):
	return a/b

div = check_b(div)

print(div(10, 0))