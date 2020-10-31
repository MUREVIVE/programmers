# 이렇게 접근하여 코드 작성했는데 많이 꼬였다.
# from collections import deque

# def solution(bridge_length, weight, truck_weights):
    
#     tw = deque(truck_weights)
#     before_T = []
#     after_T = []
    
#     # count = 0, i = 0, sum = 0, time = 0
#     # count, i, sum, time = 0
#     count = i = sum = time = 0
#     # while len(after_T) == len(truck_weights):
#     while len(after_T) != len(truck_weights):
#         sum += truck_weights[i]
#         if sum <= weight:
#             before_T.append(tw[i])
#             i += 1
#             print("b", before_T)
#         # if time == 2:
#         if time == bridge_length:
#             before_T.pop(0)
#             after_T.append(tw[i])
#             print("a", after_T)
#             time = 0
#             sum = 0
            
        
#         # time += 1, count += 1
#         # time, count += 1
#         time += 1
#         count += 1
        
#     return count


def solution(bridge_length, weight, truck_weights):
    q = [0] * bridge_length # 다리에 있는 트럭
    time = 0
    
    while q:
        time += 1
        q.pop(0)
        
        if truck_weights:
            
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return sec


def solution(bridge_length, weight, truck_weights):
    
    time = 0
    on_bridge = []
    on_time = []
    
    while truck_weights or on_bridge:
        time += 1
        if on_time: # 트럭이 들어간 시간
            if (on_time[0] + bridge_length >= time):
                on_bridge.pop(0)
                on_time.pop(0)
        
        if truck_weights:
            if (sum(on_bridge) + truck_weights <= weight):
                on_bridge.append(truck_weights.pop(0))
                on_time.append(time)
                
    return time
