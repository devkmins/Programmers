def solution(t, p):
    n = len(p)
    cnt = 0
    ans = 0
    temp = ""

    for i in range(len(t) - n + 1):
        while cnt < n:
            temp += t[cnt + i]
            cnt += 1

        if int(temp) <= int(p):
            ans += 1

        cnt = 0
        temp = ""

    return ans