valid_input = 0
for i in range(0, int(input())):
    if input().count("1") >= 2:
        valid_input += 1
print(valid_input)