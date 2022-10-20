def Fibonacci(n):
    a1 = 1
    a2 = 2
    score_list = [a1, a2]
    while True:
        a = score_list[-1] + score_list[-2]
        if a < n:
            score_list.append(a)
        else:
            break
    score = 0
    for item in score_list:
        if item % 2 == 0:
            score += item

    return score


print(Fibonacci(4000000))
