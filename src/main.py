import time

from bcc.table import Array


def any_example(any_string: str):
	print(f"This is a string: {any_string}", flush=True)


def add(*args: Array) -> int:
	result = 0
	for arg in args:
		for item in arg:
			print(item)
			result += item
	return result

if __name__ == "__main__":
	number = 0
	array = []
	while True:
		array.append(number)
		number += 1
		result = add(array)
		print(result)
		time.sleep(10)
		any_example("Version 5")
