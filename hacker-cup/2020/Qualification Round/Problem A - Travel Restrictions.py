def is_valid(source, destination, incoming, outgoing):
    return outgoing[source] == 'Y' and incoming[destination] == 'Y'


def solve_test_case(test_case):
    N = int(input())
    I = input()
    O = input()

    print('Case #' + str(test_case) + ':')

    for i in range(N):
        possible = [False for j in range(N)]
        possible[i] = True

        for j in range(i - 1, -1, -1):
            if not is_valid(j + 1, j, I, O):
                break
            possible[j] = True

        for j in range(i + 1, N):
            if not is_valid(j - 1, j, I, O):
                break
            possible[j] = True

        possible = ['Y' if possible[j] else 'N' for j in range(N)]

        print(''.join(possible))


def main():
    T = int(input())
    for test in range(1, T + 1):
        solve_test_case(test)


main()
