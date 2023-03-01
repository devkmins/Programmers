def prime(nums):
    check = [False] * (max(nums) + 1)
    prime = []
    
    for i in range(2, max(nums) + 1):
        if not check[i]:
            prime.append(i)
            j = i + i
            while j <= max(nums):
                check[j] = True
                j += i
                
    return prime

def solution(nums):
    a, b, c = 0, 1, 2
    ans = []
    cnt = 0
    
    while a < len(nums) - 2:
        if b < len(nums) - 1:
            if c < len(nums):
                ans.append(nums[a] + nums[b] + nums[c])
                c += 1
            else:
                b += 1
                c = b + 1
        else:
            a += 1
            b = a + 1
            c = b + 1
    
    prime_values = prime(ans)
    
    for i in ans:
        if i in prime_values:
            cnt += 1
        else:
            pass
        
    return cnt