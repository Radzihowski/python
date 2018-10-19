num = 9119
count = []
intToStr = str(num)
for character in intToStr:
    print(character)
    for i in range(len(count)):
        count[i] = character
print(count)

