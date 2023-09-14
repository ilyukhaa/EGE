"""№1"""
from itertools import product
cnt = 0
for x in product('012345678', repeat=6):
    k = su = 0
    for n in x:
        su += int(n)
        if int(n) % 2 != 0:
            k += 1
    if x[0] != '0' and k <= 2 and su % 6 == 0 and su % 4 != 0:
        cnt += 1
print(cnt)


"""№2"""
from itertools import product
cnt = 0
for x in product('!*!*Ш*!!!', repeat=4):
    s = ''.join(x)
    if s.count('!') + s.count('Ш') == s.count('*'):
        if '*Ш' not in s and 'Ш*' not in s:
            cnt += 1
print(cnt)


"""№3"""
from itertools import permutations
cnt = 0
for w in set(''.join(x) for x in permutations('АВТОМАТ', r=7)):
    if ('АА' not in w) and ('АО' not in w) and ('ОА' not in w):
        if all(s not in w for s in set(''.join(i) for i in permutations('ВТМТ', r=2))):
            cnt += 1
print(cnt)


"""№4"""
n = [int(x) for x in open('v4-17-1.txt')]

mi = 1000000000
for x in n:
    if abs(x) % 10 == 3:
        mi = min(mi, x)

kp = 0
ma = -1000000000
for i in range(len(n) - 1):
    if (abs(n[i]) % 10 == 3 or abs(n[i + 1]) % 10 == 3) and not(abs(n[i]) % 10 == 3 and abs(n[i + 1]) % 10 == 3):
        if n[i]**2 + n[i + 1]**2 < mi**2:
            kp += 1
            ma = max(ma, n[i]**2 + n[i + 1]**2)
print(kp, ma)


"""№5"""
n = [int(x) for x in open('v4-17-2.txt')]

k37 = []
for x in n:
    if x % 37 != 0:
        k37.append(x)
med = sum(k37)/len(k37)

kt = 0
ma = -1
for i in range(len(n) - 2):
    tr = [n[i], n[i + 1], n[i + 2]]
    sch = bin(sum(tr))[2::]
    if sch == sch[::-1] and min(tr) > med:
        kt += 1
        ma = max(ma, sum(tr))
print(kt, ma)
