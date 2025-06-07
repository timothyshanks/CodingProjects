import math
def solution(numbers):
    output = []
    for i in range(0,int(math.ceil(len(numbers) / 2))):
        x = numbers[i]
        opp = numbers[len(numbers)-i-1]
        output.append(x + opp)
    return output
    #pass

setn = list(range(2,201))
print(solution(setn))
