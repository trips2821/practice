def trailingZeros(n):
    # write your code here, try to do it without arithmetic operators.
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i

    tmp_str = f"{factorial}"

    counter = len(tmp_str) - len(tmp_str.rstrip('0'))

    return counter

def mul(n, m):
    ans = 0
    counter = 0
    while (m):
        if m % 2 == 1:
            ans += n << counter

        counter += 1
        m = int(m / 2)

    return ans


# r = mul(13, 3)
# print(r)


def trailingZeros(n):
    # write your code here, try to do it without arithmetic operators.
    factorial = 1
    for i in range(1, n + 1):
        factorial = mul(factorial, i)

    tmp_str = f"{factorial}"
    print(tmp_str)

    counter = len(tmp_str) - len(tmp_str.rstrip('0'))

    return counter

# trailingZeros(1001171717)


def digitCounts(k, n):
    count = 0
    for num in range(n + 1):
        if num == 0 and k == 0:
            count += 1

        while num:
            num, mod = divmod(num, 10)
            if mod == k:
                count += 1

    return count

# print(digitCounts(1, 12))

def dicesSum(n):
    answers = []

    for i in range(1, 7):
        answers.append([i])

    for i in range(n-1):
        new_rolls = []
        for rolls in answers:
            if len(rolls) == i+1:
                for roll in range(1, 7):
                    new_rolls.append(rolls + [roll])

        answers = new_rolls

    hit_counts = {}
    for rollset in answers:
        num = sum(rollset)
        if num in hit_counts:
            hit_counts[num] += 1
        else:
            hit_counts[num] = 1

    combinations = 6 ** n

    probs = []
    for each in hit_counts.keys():
        prob = hit_counts[each] / combinations
        probs.append([each, prob])

    return probs




print(dicesSum(3))


def findWays(rolls, num):
    # Create a table to store results of subproblems. One extra
    # row and column are used for simpilicity (Number of dice
    # is directly used as row index and sum is directly used
    # as column index). The entries in 0th row and 0th column
    # are never used.
    table = [[0] * (num + 1) for i in range(rolls + 1)]  # Initialize all entries as 0

    faces = 6

    for j in range(1, min(faces + 1, num + 1)):  # Table entries for only one dice
        table[1][j] = 1

    # Fill rest of the entries in table using recursive relation
    # i: number of dice, j: sum
    for i in range(2, rolls + 1):
        for j in range(1, num + 1):
            for k in range(1, min(faces + 1, j)):
                table[i][j] += table[i - 1][j - k]

                # print(dt)
    # Uncomment above line to see content of table

    return table[-1][-1]

def mergeSortedArray(A, B):
    total_length = len(A) + len(B)
    c = [0 for i in range(total_length)]

    a_ptr = len(A) - 1
    b_ptr = len(B) - 1

    for i in range(total_length - 1, -1, -1):
        if (a_ptr > -1 and A[a_ptr] >= B[b_ptr]) or b_ptr < 0:
            c[i] = A[a_ptr]
            a_ptr -= 1
            continue

        if (b_ptr > -1 and B[b_ptr] >= A[a_ptr]) or a_ptr < 0:
            c[i] = B[b_ptr]
            b_ptr -= 1

    return c

b = [1,2]
a = [3,4]

mergeSortedArray(a, b)
