
# divmod에 대해 배웠다.

def solution(n):
    # answer = 0
    # temp = ''
    # while True:
    #     if n == 0:
    #         break
    #     temp += str(n % 3)
    #     n //= 3
    # # answer = int(temp[::-1])
    # # temp = temp[::-1]

    answer = []
    while True:
        n, rest = divmod(n, 3)  # divmod : n을 3으로 나눈 몫과 나머지 반환
        answer.append(rest)
        if n == 0:
            break

    return sum([i * 3 ** idx for idx, i in enumerate(reversed(answer))])


#########################################################################

# 다른 풀이

def solution(n):
    answer = 0
    cnt = 1
    a = ''
    while n>0:
        a+=str(n%3)
        n = n//3
    print(a)
    for b in range(len(a),0,-1):
        answer += (int(a[b-1])*cnt)
        cnt *= 3
    return answer