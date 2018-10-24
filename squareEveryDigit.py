##num = 9119
##intToStr = str(num)
##for character in intToStr:
##    print(int(character)*int(character), end='')

num = 9119

def square_digits(num):
    return int(''.join(str(int(i)**2) for i in str(num)))
print(square_digits(num))


def square_digits1(num):
    ret = ""
    for i in str(num):
        ret += str(int(i)**2)
    return int(ret)
print(square_digits1(num))

def square_digits2(num):
    result = 0
    for character in str(num):
        result += int(character)*int(character)
    return result
print(square_digits2(num))
        
