import sys
input = sys.stdin.readline

# Minimized for fun
# 58 chars
# n=int(input());[print(f'{i^i>>1:0{n}b}')for i in range(1<<n)]

def Gray(n):
    return [format(i ^ (i >> 1), f'0{n}b') for i in range(2**n)]

def main():
	n = int(input())

	codes = Gray(n)
	for code in codes:
		print(code)

main()
