from collections import deque


def solution(n, computers):
    answer = 0
    visit = [0 for _ in range(n)]

    def dfs(start):
        # TypeError: 'int' object is not iterable
        # Q = deque(start)
        Q = deque([start])

        while Q:
            num = Q.popleft()  # popleft()는 왼쪽 원소부터 / pop()은 오른쪽 원소부터
            if visit[num] == 0:
                visit[num] = 1

            for i in range(len(computers[0])):
                if computers[num][i] == 1 and visit[i] == 0:
                    Q.append(i)

    i = 0
    # for i in visit: # 이렇게 하면 visit배열에 0이 남아있을 수도 있음.
    while 0 in visit:  # visit 배열에 0이 없을 때 까지 진행해야 함.
        if visit[i] == 0:
            dfs(i)
            answer += 1
        i += 1
    return answer