def cal_dist(num, now_l, now_r, pos, HANDED):
    X, Y = 0, 1
    dist_l = abs(pos[now_l][X] - pos[num][X]) + abs(pos[now_l][Y] - pos[num][Y])
    dist_r = abs(pos[now_r][X] - pos[num][X]) + abs(pos[now_r][Y] - pos[num][Y])

    # 거리가 같으면
    if dist_l == dist_r:
        return 'R' if HANDED == 'right' else 'L'
    return 'R' if dist_l > dist_r else 'L'


def solution(numbers, hand):
    answer = ''

    # 왼손잡이 또는 오른손 잡이
    HANDED = hand

    # 번호 좌표화
    position = {1: (0, 0), 2: (0, 1), 3: (0, 2),
                4: (1, 0), 5: (1, 1), 6: (1, 2),
                7: (2, 0), 8: (2, 1), 9: (2, 2),
                '*': (3, 0), 0: (3, 1), '#': (3, 2)}

    # 왼쪽 숫자, 오른쪽 숫자
    left_num, right_num = set([1, 4, 7]), set([3, 6, 9])

    # 손 위치 초기화
    now_l, now_r = '*', '#'

    for num in numbers:
        if num in left_num:  # 왼쪽 키라인
            answer += 'L'
            now_l = num
        elif num in right_num:  # 오른쪽 키라인
            answer += 'R'
            now_r = num
        else:  # 중간 키라인
            answer += cal_dist(num, now_l, now_r, position, HANDED)
            if answer[-1] == 'L':  # 현재 손잡이 최신화
                now_l = num
            else:
                now_r = num

    return answer