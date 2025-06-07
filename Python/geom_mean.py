import numpy as np

def solution(numbers):
    output = []
    for i in range(0,len(numbers)):
        x = numbers[i]
        opp = numbers[len(numbers)-i-1]
        output.append((x, round(np.sqrt(x*opp),2)))
    return output
    #pass

setn = list(range(1,101))
#setn = [1:100]
print(solution(setn))
