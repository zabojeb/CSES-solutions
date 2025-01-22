from math import floor

import sys
input = sys.stdin.readline

def main():
	n = int(input())

	mult = 5
	answer = 0
	while mult <= n:
		answer += floor(n / mult)
		mult *= 5

	print(answer)

main()
