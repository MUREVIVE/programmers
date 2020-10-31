def solution(n):
    
    lst = [[0] * n for _ in range(n)]
    # 남 동 북
    dy = [1, 0, -1]
    dx = [0, 1, -1]
    i = 0
    num = 1
    y = x = 0
    answer = []
    
    while n > 0:
        for j in range(n):
            lst[y][x] = num
            num += 1
            # 범위 벗어날 시
            if j < n-1:
                y = y + dy[i]
                x = x + dx[i]
            # n-1번째가 되면 방향 전환
            else:
                # i == 2일 경우 방향 리스트 내에서 마지막이므로 북 -> 남으로 전환
                if i == 2:
                    i = 0
                    y = y + dy[i]
                    x = x + dx[i]
                else: # 그렇지 않은 경우
                    i += 1
                    y = y + dy[i]
                    x = x + dx[i]
                    
        n -= 1
    
    for i in range(len(lst)):
        for j in range(len(lst)):
            if lst[i][j] != 0:
                answer.append(lst[i][j])
                
    return answer


    ####################################################################

    # 다른 풀이

    import itertools


def get_next(cur_y, cur_x, cur_d):
    DELTAS = {'U': (-1, -1), 'D': (1, 0), 'R': (0, 1)}
    dy, dx = DELTAS[cur_d][0], DELTAS[cur_d][1]
    nxt_y, nxt_x = cur_y + dy, cur_x + dx
    return nxt_y, nxt_x


def check_turn(nxt_y, nxt_x, n, snail):
    return nxt_y < 0 or nxt_y >= n or nxt_x > nxt_y or snail[nxt_y][nxt_x] != 0


def solution(n):
    NEXT = {'U': 'D', 'D': 'R', 'R': 'U'} # dictionary
    N = sum(range(1, n+1))
    
    snail = [[0] * i for i in range(1, n+1)]
    
    cur_y, cur_x, cur_d = 0, 0, 'D' # cur_d : 방향
    for num in range(1, N+1):
        snail[cur_y][cur_x] = num # 현재 좌표 값에 num 대입
        if check_turn(*get_next(cur_y, cur_x, cur_d), n, snail): # 범위 조건에 벗어난다면
            cur_d = NEXT[cur_d] # 
        cur_y, cur_x = get_next(cur_y, cur_x, cur_d)

    return list(itertools.chain(*snail))