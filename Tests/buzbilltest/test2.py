def programmerStrings(s):
    ans = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'e', 'r']
    anssum = len(s) - 2

    cnt = 0
    for i in s:
        if i in ans:
            ans.remove(i)
            if not ans:
                break
        cnt += 1
    anssum -= cnt

    reverseS = s[::-1]
    cnt = 0
    ans = ['p', 'r', 'o', 'g', 'r', 'a', 'm', 'm', 'e', 'r']

    for i in reverseS:
        if i in ans:
            ans.remove(i)
            if not ans:
                break
        cnt += 1

    anssum -= cnt

    return anssum


s = "xprogxrmaxemrppprmmograeiruu"
print("answe", programmerStrings(s))
