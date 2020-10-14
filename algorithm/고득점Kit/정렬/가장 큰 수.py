def solution(numbers):
    """
    for i in range(len(numbers)-1):
        temp = ''
        for j in range(i+1, len(numbers)):
            if numbers[i] == 0:
                pass
            temp 
    """

    numbers = list(map(str, numbers))  # numbers안에 모든 요소를 str형태로 바꾼후 다시 list로 저장
    numbers.sort(key=lambda x: x * 3, reverse=True)  # 1000이하의 수니깐 3자리수까지 맞춰줌
    if sum(list(map(int, numbers))) == 0:  # 만약 numbers의 모든수의 합이 0이면
        numbers = list(set(numbers))  # numbers에 set(numbers)를 대입

    return ''.join(numbers)


#################################################################

# 다른 풀이

import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer