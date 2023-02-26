from collections import deque

def solution(priorities, location):
    queue = deque(priorities)
    cnt, max_val, loc = 0, max(queue), location

    while queue:
        if loc == 0:
            if queue[0] == max_val:
                cnt += 1
                return cnt
            elif queue[0] != max_val:
                loc = len(queue) - 1
                queue.append(queue.popleft())
        elif loc > 0:
            if queue[0] == max_val:
                queue.popleft()
                cnt += 1
                loc -= 1
                max_val = max(queue)
            elif queue[0] != max_val:
                queue.append(queue.popleft())
                loc -= 1