from collections import deque
import sys

def solution(queue1, queue2):
    answer = 0
    N = len(queue1)
    q1, q2 = deque(queue1), deque(queue2)
    maximum = N*(N-1)
    
#     def backtracking(sum1, sum2, cnt):
        
#         if sum1 == sum2:
#             nonlocal answer
#             answer = min(answer, cnt)
#             return
        
#         if cnt >= answer:
#             return
        
#         if not queue1 or not queue2:
#             return
        
#         if sum1 > sum2:
#             num = queue1.pop(0)
#             queue2.append(num)
#             backtracking(sum1-num, sum2+num, cnt+1)
        
#         else:
#             num = queue2.pop(0)
#             queue1.append(num)
#             backtracking(sum1+num, sum2-num, cnt+1)
    
#     backtracking(sum(queue1), sum(queue2), 0)

    sum1, sum2 = sum(q1), sum(q2)
    while sum1 != sum2:
        if not q1 or not q2 or answer > N*4:
            break
        if sum1 > sum2:
            num = q1.popleft()
            q2.append(num)
            sum1, sum2 = sum1-num, sum2+num
        else:
            num = q2.popleft()
            q1.append(num)
            sum1, sum2 = sum1+num, sum2-num
        answer += 1
    
    return answer if sum1 == sum2 else -1