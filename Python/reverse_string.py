def solution(numbers):
    output = []
    for i in range(0,len(numbers)):
        x = numbers[i]
        rev = int(str(x)[::-1])
        if rev in numbers:
            output.append((x, rev))
    return output
    #pass

setn = list(range(2,201))
print(solution(setn))
