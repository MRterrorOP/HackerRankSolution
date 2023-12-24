# from bs4 import BeautifulSoup
# soup = BeautifulSoup('html.parser')
# print(soup.text)
def greet(func):
	func()
def greet2():
	def func():
		return 15
	return func()
a = greet2()
print(a)