from itertools import product
from itertools import permutations
from itertools import combinations
from itertools import groupby
'''a = list(map(int, input().split()))
b = list(map(int, input().split()))
l = list(product(a, b))
for i in l:
    print(i, end=" ")

print("\n")
print(list(product(a, repeat=2)))

nasted_list = [[1, 2, 3], [4, 5]]
print(list(product(*nasted_list)))'''

'''a, b = map(str, input().split())
b = int(b)
result = sorted(list(permutations(a, b)))
for i in result:
    string = ""
    for x in i:
        string = string + x
    print(string)'''

# a, b = map(str, input().split())
# b = int(b)
# n = 1
# L = []
# l = []
# for i in range(b):
#     m = sorted(list(combinations(a, n)))
#     p = []
#     for x in m:
#         p.append(sorted(x))
#     L = L + sorted(p)
#     n += 1
#
#
# for i in L:
#     string = ""
#     for x in i:
#         string = string + x
#     print(string)

n = input()
for i,j in groupby(n):
    print(tuple([len(list(j)), int(i)]),end=" ")