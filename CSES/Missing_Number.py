import sys
input = sys.stdin.readline

def main():
	n = int(input())
	nums = set(map(int, input().split()))

	print(list(set(range(1, n + 1)) - nums)[0])

main()
