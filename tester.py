# Kees Hartley 2027

import time
import random
import pickle

digits = open("million_digits.txt").read()
your_attempt = input("enter your digits of pi after the point\n: 3.")
failed = False

for i, digit in enumerate(your_attempt):
	correct_digit = digits[i]
	print(f"correct digit: {correct_digit}")
	print(f"your digit   : {digit}")
	
	if digit != correct_digit:
		print(digits[:i+1], "<- correct") 
		print(your_attempt[:i+1], "<- your attempt")
		print(" " * i + "^")
		print(f"silly alien! you made an error. digit {i} is {correct_digit}, not {digit}")
		failed = True
		break

	print(digits[:i+1])
	print()
	
if not failed:
	print(f"you succeeded in listing {len(your_attempt)} digits of pi")
	if len(your_attempt) >= 1000:
		print(pickle.load(open("winmsg.pkl", "rb")))


