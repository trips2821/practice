
def make_perms(l, n):
    if n == 0:
        return

    for c in l:



def p(l):
    perms = make_perms(l, len(l))
    return perms

l = [1,2,3]

ps = p(l)

print(ps)
