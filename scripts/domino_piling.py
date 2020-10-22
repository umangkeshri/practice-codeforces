# problem link: https://codeforces.com/problemset/problem/50/A
from functools import reduce

total = reduce(lambda x, y: x * y, [int(x) for x in input().split(" ")])
print((total - (total % 2)) // 2)