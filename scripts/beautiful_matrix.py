# Problem link : https://codeforces.com/problemset/problem/263/A

moves = 0

for index in range(0, 5):
    a = [int(i) for i in input().split(" ")]
    if 1 in a:
        j = a.index(1)
        moves += abs(3 - (j+1))
        moves += abs(3 - (index+1))
        break
print(moves)
