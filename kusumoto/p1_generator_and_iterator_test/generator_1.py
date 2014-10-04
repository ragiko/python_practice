'''
ジェネレータを用いてフィボナッチ数列を出力する
'''

def fibonacci_with_generator(max):
	'''def fibonacci_with_generator()

	フィボナッチ数列を出力するジェネレータ。
	なおこの文章は関数の属性の一つである__doc__を呼び出すことで参照することが出来る。
	'''
	a, b = 0, 1
	while a < max:
		yield a
		a, b = b, a+b


if __name__ == '__main__':

	print(fibonacci_with_generator.__doc__)				#fibonacci_with_generator()のdocstringを呼び出す

	for sequence in fibonacci_with_generator(1000):
		print("{0} ".format(sequence))					#1000未満のフィボナッチ数を出力する
