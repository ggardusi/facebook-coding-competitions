#include <bits/stdc++.h>

void solve_test_case(const int test_case, const int N, const int M, const std::vector<int> &C)
{
    std::vector<long long int> dp(N, LLONG_MAX);
    std::multiset<long long int> available;

    dp[N - 1] = 0;
    available.insert(dp[N - 1]);

    for (int i = N - 2; i >= 0; i -= 1)
    {
        const int previous = i + M + 1;
        if (previous < N)
        {
            const auto it = available.find(dp[previous]);
            assert(it != available.end());
            available.erase(it);
        }

        if (i == 0)
        {
            break;
        }

        assert(!available.empty());
        const long long int best = *available.begin();

        dp[i] = (best == LLONG_MAX or C[i] == 0) ? LLONG_MAX : best + C[i];
        available.insert(dp[i]);
    }

    assert(!available.empty());
    dp[0] = *available.begin();
    if (dp[0] == LLONG_MAX)
    {
        dp[0] = -1;
    }

    std::cout << "Case #" << test_case << ": " << dp[0] << std::endl;
}

int main()
{
    std::ios_base::sync_with_stdio(0);
    std::cin.tie(0);
    std::cout.tie(0);

    int T;
    std::cin >> T;

    for (int test_case = 1; test_case <= T; test_case += 1)
    {
        int N, M;
        std::cin >> N >> M;

        std::vector<int> C(N);
        for (int &i : C)
        {
            std::cin >> i;
        }

        solve_test_case(test_case, N, M, C);
    }

    return 0;
}
