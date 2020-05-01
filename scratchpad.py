
# n = 100
#
# for a in range(1, n):
#     for b in range(1, n):
#         for c in range(1, n):
#             for d in range(1, n):
#                 if a ** 3 + b ** 3 == c ** 3 + d ** 3:
#                     print(a, b, c, d)

n= 100
mapi = {}
for a in range(1, n):
    for b in range(1, n):
        result = a ** 3 + b ** 3
        if result in mapi:
            mapi[result] = mapi[result] + [a,b]
        else:
            mapi[result] = [a,b]

for result in mapi:
    question = mapi[result]
    if len(question) != 4 and len(question) != 2:
        print(question)
