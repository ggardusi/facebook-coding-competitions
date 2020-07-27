from collections import defaultdict


def solve(v):
    chop_l = defaultdict(int)
    chop_r = defaultdict(int)

    for i in sorted(v, reverse=True):
        L = i[0]
        R = i[1]
        side = i[2]
        if side == 0:
            chop_l[L] = max(chop_l[L], chop_l[R] + (R - L))

    for i in sorted(v):
        L = i[0]
        R = i[1]
        side = i[2]
        if side == 1:
            chop_r[R] = max(chop_r[R], chop_r[L] + (R - L))

    indexes = []
    indexes.extend(chop_l.keys())
    indexes.extend(chop_r.keys())

    ans = 0
    for i in indexes:
        ans = max(ans, chop_r[i] + chop_l[i])

    return ans


def solve_test_case(test_case):
    N = int(input())

    v = []
    for i in range(N):
        P, H = list(map(int, input().split()))
        v.append((P - H, P, 0))
        v.append((P, P + H, 1))

    print('Case #' + str(test_case) + ': ' + str(solve(v)))


def main():
    T = int(input())
    for test in range(1, T + 1):
        solve_test_case(test)


main()
