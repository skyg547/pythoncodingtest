# https://www.acmicpc.net/problem/1264
# 모음의갯수

if __name__ == '__main__':
    vowel = ['a', 'e', 'i', 'o', 'u']
    while True:
        strings = input().lower()
        if strings[0] == '#':
            break

        print(len(list(filter(lambda x: x in vowel, list(strings)))))
        list(strings)
