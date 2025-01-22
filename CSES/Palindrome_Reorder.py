from collections import Counter

import sys
input = sys.stdin.readline

def main():
	c = Counter(input().strip())

	odd_element = None

	if sum(c.values()) % 2 == 0:
		for key in c:
			if c[key] % 2 != 0:
				print("NO SOLUTION")
				return
	else:
		for key in c:
			if c[key] % 2 != 0:
				if odd_element:
					print("NO SOLUTION")
					return
				else:
					odd_element = key

	answer = ""
	for key in c:
		v = c[key]
		if v % 2 != 0:
			continue
		else:
			answer += key * (v // 2)

	if odd_element:
		print(answer + (odd_element * c[odd_element]) + "".join(reversed(answer)))
	else:
		print(answer + "".join(reversed(answer)))

main()
