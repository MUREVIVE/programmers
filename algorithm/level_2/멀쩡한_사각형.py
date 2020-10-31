# 접근 방법이 잘못 됐음. 너무 단순하게 생각. 최소공약수를 생각해야 했음.

# if w == h:
#         answer = w * h - w
#     elif w < h:
#         answer = w * h - (2 * w)
#     else:
#         answer = w * h - (2 * h)

def solution(w,h):
    answer = 0
    
    def gcd(a, b):
        if b == 0: return a
        return gcd(b, a % b)
    
    if w == h:
        return (w * h) - w
    
    elif w < h:
        l = h
        s = w
    else:
        l = w
        s = h
    
    g = gcd(l, s)
        
    return w*h - (w+h-g)