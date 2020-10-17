
def solution(n):
    answer = 0

    for i in str(n):
        answer += int(i)

    return answer

###################################################################

# 다른 풀이

def sum_digit(number):
    if number < 10:
        return number;
    return (number % 10) + sum_digit(number // 10)