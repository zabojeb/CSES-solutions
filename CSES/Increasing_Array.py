import sys
input = sys.stdin.readline

def main():
	n = int(input())
	a = list(map(int, input().split()))

	answer = 0
	prev = a[0]
	for i in range(1, n):
		current = a[i]
		if current < prev:
			answer += prev - current
		else:
			prev = current

	print(answer)

main()
