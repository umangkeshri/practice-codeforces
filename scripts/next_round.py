# Problem link: https://codeforces.com/problemset/problem/158/A\

n, k = [int(x) for x in input().split(" ")]
a = [int(x) for x in input().split(" ")]
score = a[k-1]
count = 0
for i, elem in enumerate(a):
    if elem >= score and elem > 0:
        count += 1 
print(count)

