import re

# p = re.compile('[a-z]')
low = ['qazwsxedcrfvtgbynhujmiklop0123456789-_.']


def solution(new_id):
    answer = ''

    new_id = new_id.lower()

    for i in range(len(new_id)):
        if new_id[i] not in low:
            print(new_id.replace(new_id[i], ''))

    # if re.search(p):

    while 1:
        print(1)
        if '...' in new_id:
            new_id.replace('...', '.')
        elif '..' in new_id:
            new_id.replace('..', '.')
        else:
            break
    if new_id[0] == '.':
        del new_id[0]

    if new_id == '':
        new_id = 'a'

    if len(new_id) >= 16:
        new_id = new_id[:15:]

    if new_id[len(new_id) - 1] == '.':
        del new_id[len(new_id) - 1]

    if len(new_id) <= 2:
        for index in range(len(new_id) - 1, 3):
            new_id += new_id[len(new_id) - 1]

    return answer


if __name__ == '__main__':
    s = "...!@BaT#*..y.abcdefghijklm"
    print(solution(s))
