from collections import deque

import sys
input = sys.stdin.readline

def main():
	n = int(input())
	if n == 1:
		print(1)
		return

	if n == 4:
		print(*[2, 4, 1, 3])
		return

	if n < 5:
		print("NO SOLUTION")
		return

	answer = deque([4, 2, 5, 3, 1])
	for x in range(6, n + 1):
		left = answer[0]
		right = answer[-1]

		left_diff = abs(left - x)
		right_diff = abs(right - x)

		if left_diff > 1:
			answer.appendleft(x)
		elif right_diff > 1:
			answer.append(x)
		else:
			print("NO SOLUTION")
			return

	print(*answer)

main()
