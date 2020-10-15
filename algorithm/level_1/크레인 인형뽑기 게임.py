def solution(board, moves):
    answer = 0
    stacklist = []

    for i in moves:  # col에 대한 정보 다루는거라 생각하기
        for j in range(len(board)):
            if board[j][i - 1] != 0:  # 해당 board 칸에 인형이 있다면
                stacklist.append(board[j][i - 1])
                board[j][i - 1] = 0

                if len(stacklist) > 1:
                    if stacklist[-1] == stacklist[-2]:  # 윗부분에 쌓인 두개의 인형이 같은 것이라면
                        stacklist.pop(-1)
                        stacklist.pop(-1)
                        answer += 2
                # 해당 board[j][i-1] 인형에 대해 처리를 했다면 다음 moves 처리를 위해 break.
                # 안하면 해당 col내 다른 row에 있는 인형 처리를 해버릴 수 있기 때문.
                break

    return answer