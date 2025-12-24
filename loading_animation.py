import time
import random

# Global flag to prevent multiple error retries
error_happened = False

GREEN = '\033[92m'
RED = '\033[91m'
DARK_RED = '\033[38;2;97;6;0m'
ROYAL_BLUE = '\033[38;2;65;105;225m'
RESET = '\033[0m'
DOWN = '\033[1B'
UP = '\033[F'
CLEAR = '\033[K'

def summon_loading_bar():
	length = 1
	# create a placeholder line for the bar then move down
	print()

	for i in range(1, 51):
		# move up to the placeholder line created above
		print(UP, end='')
		# print red bar and clear remainder of line
		print(f"{RED}[{'#' * length:50}] {i*2}.0 % {RESET}{CLEAR}")
		time.sleep(0.1)

		if random.randint(0, 15) == 7:
				time.sleep(0.7)
		length += 1

	# when loop ends delete old bar/line and replace a new one with green
	print(UP, end='')
	print(f"{GREEN}[{'=' * 50}] 100.0 % {RESET}{CLEAR}")

	# move down so next bar starts under this one
	global error_happened
	if random.randint(0, 30) == 15 and not error_happened:
		print(DOWN, end='')
		print(UP, end='')
		print(f"{RED}[{'#' * 50}] INCOMPLETE {RESET}{CLEAR}")
		print(f"{RED}Error or Issue Found! Retrying...{RESET}{CLEAR}")
		error_happened = True  # Set flag before recursion to prevent further retries
		summon_loading_bar()
		time.sleep(0.5)
