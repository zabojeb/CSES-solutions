from itertools import permutations

import sys
input = sys.stdin.readline

# Minimized for fun
# 100 chars
# from itertools import*;s=input();r={''.join(p)for p in permutations(s)};print(len(r),*sorted(r),sep='\n')

def main():
	s = input().strip()

	perms = {"".join(perm) for perm in permutations(s)}

	print(len(perms))
	for perm in sorted(perms):
		print(perm)

main()
