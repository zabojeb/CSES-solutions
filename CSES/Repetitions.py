import sys
input = sys.stdin.readline

def main():
	s = input()

	answer = 0
	counter = 0
	for i in range(len(s)):
		if i == 0:
			counter += 1

		elif s[i] == s[i - 1]:
			counter += 1

		else:
			counter = 1

		answer = max(answer, counter)

	print(answer)

main()
