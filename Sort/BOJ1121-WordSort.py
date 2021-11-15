def solution(arrays):
    print(sorted(arrays, key=lambda x: ((len(x)), min(x[0]))))
    return sorted(arrays, key=lambda x: (-(len(x)), min(x)))


print(solution(["ab", "cd", "b"]))
