import time


def any_example(any_string):
	print(f"This is a string: {any_string}", flush=True)


if __name__ == "__main__":
	while True:
		time.sleep(10)
		any_example("Version 5")
