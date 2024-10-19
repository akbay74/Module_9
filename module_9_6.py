from itertools import combinations

def all_variants(text):
    for i in range(1, len(text)+1):
        substring = []
        comb = combinations(text, i)
        substring.extend(comb)
        for j in substring:
            j = list(j)
            yield (''.join(j))


a = all_variants("abc")
for i in a:
    if i == 'ac':
        continue
    print(i)