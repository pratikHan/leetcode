import time
start = time.time()
def solution(s):
    ls = ''
    l = 0
    for c in s:
        if c in ls:
            if len(ls) > l:
                l = len(ls)
            ls = ls[ls.index(c) + 1:]
        ls += c
    if len(ls) > l:
        l = len(ls)
    return l


print(solution("abcabcabc"))
end = time.time()
final = end - start
print(final)