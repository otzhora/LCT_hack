def max_value_of_an_expression(nums, ops):
    operations = {
        "+": lambda x, y: x + y,
        "-": lambda x, y: x - y,
        "*": lambda x, y: x * y
    }

    n = len(nums)

    m = [[0 for _ in range(n)] for _ in range(n)]
    M = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        m[i][i] = nums[i]
        M[i][i] = nums[i]

    def MinMax(i, j):
        mi = 10**9
        ma = -10**9

        for k in range(i, j):
            a = operations[ops[k]](M[i][k], M[k + 1][j])
            b = operations[ops[k]](M[i][k], m[k + 1][j])
            c = operations[ops[k]](m[i][k], M[k + 1][j])
            d = operations[ops[k]](m[i][k], m[k + 1][j])
            mi = min(mi, a, b, c, d)
            ma = max(ma, a, b, c, d)

        return mi, ma

    for s in range(1, n):
        for i in range(n - s):
            j = i + s
            m[i][j], M[i][j] = MinMax(i, j)

    return M[0][-1]


nums = list(map(int, input().split()))
ops = input().split()

print(max_value_of_an_expression(nums, ops))
