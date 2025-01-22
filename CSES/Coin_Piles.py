import sys
input = sys.stdin.readline

def main():
	t = int(input())
	for _ in range(t):
		a, b = map(int, input().split())
		ax, bx = a % 2, b % 2

		if ax == 0 and bx == 0:
			print("NO")
		elif ax == 1 and bx == 1:
			print("YES")
		elif ax == 0 and bx == 1:
			print("YES")
		else:
			print("NO")

main()
