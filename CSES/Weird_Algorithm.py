import sys
input = sys.stdin.readline

def f(n, answer):
	answer.append(n)
	if n == 1:
		return answer

	if n % 2 == 0:
		return f(n // 2, answer)
	else:
		return f(3 * n + 1, answer)

def main():
	n = int(input())
	print(*f(n, []))

main()
