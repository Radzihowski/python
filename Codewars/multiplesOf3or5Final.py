def solution(number):
    sum = 0
    i = 0
    while i < number:
        if i%3 == 0:
            sum = sum + i
            i = i + 1
        elif i%5 == 0:
            sum = sum + i
            i = i + 1
        else:
            i = i + 1
    return(sum)

