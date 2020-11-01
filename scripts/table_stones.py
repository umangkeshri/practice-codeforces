n = int(input())
stones = input()
moves = 0

for i in range(0, n):
    if i+1 < n:
        if stones[i] == stones[i+1]:
            moves += 1

print(moves)