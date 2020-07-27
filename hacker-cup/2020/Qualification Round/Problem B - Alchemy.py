def solve(a, b):
    return max(a, b) - min(a, b) == 1


def solve_test_case(test_case):
    N = int(input())

    a = 0
    b = 0

    for c in input():
        if c == 'A':
            a += 1
        else:
            b += 1

    print('Case #' + str(test_case) + ': ' + ('Y' if solve(a, b) else 'N'))


def main():
    T = int(input())
    for test in range(1, T + 1):
        solve_test_case(test)


main()
