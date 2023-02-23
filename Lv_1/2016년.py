def solution(a, b):
    months = [3, 1, 3, 2, 3, 2, 3, 3, 2, 3, 2, 3]
    days = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
    ans = (sum(months[:(a - 1)]) + b - 1) % 7
    
    return days[ans - 2]