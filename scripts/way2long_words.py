cases = int(input())

for i in range(cases):
    word = input()
    n = len(word)
    if n > 10:
        print(f'{word[0]}{n-2}{word[-1]}')
    else:
        print(word)