
import math

def solution(progresses, speeds):
    answer = []
    #     count_list = []
    #     while
    #         count_list[i] += speeds[i]

    # 각 progresses에 대해 걸리는 시간
    check = [ math.ceil((100 - x ) /y) for x, y in zip(progresses, speeds)]

    while(len(check) > 0):
        cnt = 1
        a = check.pop(0)
        check1 = check.copy()

        for i in range(len(check)):
            if a >= check[i]:
                cnt += 1
                # 계산한 내역 빼줘야 함
                check1.pop(0)
            else:
                break

        answer.append(cnt)
        check = check1.copy()
    return answer


#################################################################

# 다른 풀이
def solution(progresses, speeds):
    print(progresses)
    print(speeds)
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer