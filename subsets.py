
ss = []
s = []
def subsets(l, n=0):
    if n == len(l):
        if s: ss.append(s[:])
        return

    c = l[n]
    s.append(c)
    subsets(l, n+1)

    s.pop(-1)
    subsets(l, n+1)


subsets(['a','b','c'])
print(ss)
