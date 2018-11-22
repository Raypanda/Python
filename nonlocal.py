def foo():
	b = 123
	def bar():
		nonlocal b
		b = 456
		print(b)
	bar()
	print(b)
foo()
print(要不要认识一下？)
print(说实话！)
