from __future__ import print_function
import numpy as np

def main():
	print("hello World")
	movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Palin", "John Cleese",
		"Terry Gilliam", "Eric Idle", "Terry Jones"]]]

	# for elem in movies:
	# 	print(elem)

#print all nested items from movies

	# for elem in movies:
	# 	if isinstance(elem, list):
	# 		for nest_1 in elem:
	# 			if isinstance(nest_1, list):
	# 				for nest_2 in nest_1:
	# 					print(nest_2)
	# 			else:
	# 				print(nest_1)
	# 	else:
	# 		print(elem)

#use Recursive function print_all

	print_all(movies)
	print_all(movies, True, 2)
	print_all(movies, False, 2)
	return (0)

def print_all(the_list, indent=False, level=0):
	"""This function takes a positional argument called "the_list", which is any Python list ( of - possibley - nested lists ).Each data item in the provided list is (recursively) printed to the screen on it's onw line. print_lol"""
	for elem in the_list:
		if isinstance(elem, list):
			print_all(elem, indent,  level + 1)
		else:
			if indent == True:
				for tab_stop in range(level):
					print("\t", end='')
			print(elem)
	
if __name__ == "__main__":
	main()
