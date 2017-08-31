import os

def func():
	"""docstring for func"""
	try:
		data = open('sketch.txt')
		for each_line in data:
			try:
				(role, line_spoken) = each_line.split(':', 1)
				print(role, end='')
				print('said: ', end='')
				print(line_spoken, end='')
			except:
					pass
		data.close()
	except:
		print("The file is missing!!")


if __name__ == "__main__":
	func()
	
