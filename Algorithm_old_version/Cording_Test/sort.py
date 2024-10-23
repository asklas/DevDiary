def solution(X, Y):
    answer = ''
    common_chars = []

    for char in X:
        if char in Y:
            common_chars.append(char)
            Y = Y.replace(char, '', 1)

    common_chars.sort(reverse=True)
    answer = ''.join(common_chars)
    if answer == "":
        answer = '-1'
    elif int(answer) == 0:
        answer = '0'
    return answer
