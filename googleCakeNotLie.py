def solution(a: str) -> int:
    possible = []
    for i in range(len(a)):
        if len(a) % (i+1) == 0:
            possible.append(i+1)
    possible.reverse()
    print(possible)
    for dividers in possible:
        if a[0:dividers] == a[dividers:dividers*2]:
            final = len(a)/dividers
        else:
            final = 1
    return int(final)

solution("ashajhsdfjbdsfjk")