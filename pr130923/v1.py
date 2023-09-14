"""№1"""
from itertools import product
cnt = 0
for x in product('01234', repeat=5):
    s = ''.join(x)
    k = 0
    for i in range(len(s) - 1):
        if abs(int(s[i]) - int(s[i + 1])) >= 2:
            k += 1
    if s[0] != '0' and k == 4:
        cnt += 1
print(cnt)


"""№2"""
from itertools import product
cnt = 0
for x in product('!*!*Ш*!!!', repeat=6):
    s = ''.join(x)
    if s.count('!') + s.count('Ш') == s.count('*'):
        if '*Ш' not in s and 'Ш*' not in s:
            cnt += 1
print(cnt)


"""№3"""
from itertools import permutations
cnt = 0
for x in set(''.join(x) for x in permutations('АТТЕСТАТ', r=8)):
    if any(i in x for i in set(''.join(i) for i in permutations('АЕА', r=2)))\
            or any(j in x for j in set(''.join(j) for j in permutations('ТТСТТ', r=2))):
        cnt += 1
print(cnt)


"""№4"""
n = [int(x) for x in open('v1-17-1.txt')]

ma = -1000000000
for x in n:
    if abs(x) % 10 == 9:
        ma = max(ma, x)

kp = 0
mas = -1000000000
for i in range(len(n) - 1):
    if (abs(max(n[i], n[i + 1])) % 10 == 2) and (n[i]**2 + n[i + 1]**2 < ma**2):
        kp += 1
        mas = max(mas, n[i]**2 + n[i + 1]**2)
print(kp, mas)


"""№5"""
def p(x):
    xn = ''
    while x > 0:
        xn = str(x % 7) + xn
        x //= 7
    return xn == xn[::-1]

n = [int(x) for x in open('v1-17-2.txt')]

k11 = []
for x in n:
    if x % 11 == 0:
        k11.append(x)
med = sum(k11)/len(k11)

kt = 0
mi = 1000000000
for i in range(len(n) - 2):
    tr = [n[i], n[i + 1], n[i + 2]]
    if p(sum(tr)) and sum(tr)/3 < med:
        kt += 1
        mi = min(mi, sum(tr))
print(kt, mi)
