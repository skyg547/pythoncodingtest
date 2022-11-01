# https://www.acmicpc.net/problem/9093
#
# 단어 뒤집기

if __name__ == '__main__':
    n = int(input())
    words = [input() for _ in range(n)]
    #  단어를 쪼개서 뒤집고 다시 합친다
    for reversedWord in list(
            map(lambda word: ' '.join(list(map(lambda string: ''.join(list(reversed(string))), word.split()))), words)):
        print(reversedWord)
