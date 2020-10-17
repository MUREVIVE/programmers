def solution(seoul):
    answer = ''

    for idx in range(len(seoul)):
        if seoul[idx] == "Kim":
            answer = '김서방은 {}에 있다'.format(idx)

    return answer


#########################################################

# 다른 풀이 - list타입 seoul에 index를 사용

def findKim(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))