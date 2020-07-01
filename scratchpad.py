def fib_rec(n, buff):
    if n == 0: return 1
    if n == 1: return 2

    if buff[n] != -1:
        return buff[n]
    else:
        buff[n] = fib_rec(n-1, buff) + fib_rec(n-2, buff)
        return buff[n]


def fib(n):
    buff = []

    for i in range(0, n+2):
        if i < 2:
            buff.append(i)
        else:
            buff.append(buff[i-1] + buff[i-2])

    return buff[n+1]


from functools import lru_cache

@lru_cache()
def fib_no(n):
    if n == 0:
        return 1
    if n == 1:
        return 2

    num = fib_no(n-1) + fib_no(n-2)

    return num

# import sys
# rl = sys.getrecursionlimit()
# sys.setrecursionlimit(rl * 10)
# print(fib_no(3000))



from itertools import permutations

# for n, i in enumerate(permutations([1,2,3,4,5])):
#     print(n, i)

ans = []
def find_num_ways(amount, dominations, d_list=[]):
    count = 0

    for d in dominations:
        tmp_amt = amount - d
        if tmp_amt == 0:
            count += 1
            tmp = d_list+[d]
            ans.append(tmp)
            # tmp.sort()
            # if tmp not in ans:
            #     ans.append(tmp)
        elif tmp_amt > 0:
            count += find_num_ways(tmp_amt, dominations, d_list + [d])

    return count

d = [1,2,3]
#print(find_num_ways(4, d))


def change_possibilities_top_down(amount_left, denominations, current_index=0):
    if amount_left == 0:
        return 1

    if amount_left < 0:
        return 0

    if current_index == len(denominations):
        return 0

    print("checking ways to make %i with %s" % (
        amount_left,
        denominations[current_index:],
    ))

    current_coin = denominations[current_index]
    # See how many possibilities we can get
    # for each number of times to use current_coin
    num_possibilities = 0
    while amount_left >= 0:
        num_possibilities += change_possibilities_top_down(
            amount_left,
            denominations,
            current_index + 1,
        )
        amount_left -= current_coin

    return num_possibilities

#print(change_possibilities_top_down(7, d,))

def backspaceCompare(S: str, T: str) -> bool:
    def remove_char(string):
        index = string.find('#')
        tmp = string[0:index-1] + string[index + 1:]
        return tmp

    while True:
        if '#' in S:
            S = remove_char(S)
        else:
            break

    while True:
        if '#' in T:
            T = remove_char(T)
        else:
            break

    return S == T

# backspaceCompare('ab#c', 'ad#c')

# from itertools import permutations
#
# for e in permutations([1,2,3,4,5], 3):
#     print(e)

def ks(w, i):
    global items
    if w == 0 or i == -1:
        return 0

    value_if_item_added, value_if_item_not_added = 0,0

    item_value = items[i][0]
    item_weight = items[i][1]
    if w >= item_weight:
        value_if_item_added = item_value + ks(w-item_weight, i-1)

    value_if_item_not_added = ks(w, i-1)

    return max(value_if_item_added, value_if_item_not_added)

items = [(5,5), (2,1), (3,2), (10,5)]
w_limit = 12
print(ks(w_limit, len(items)-1))
