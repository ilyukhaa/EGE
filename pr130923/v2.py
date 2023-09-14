"""№1"""
def p(x):
    if x > 1:
        for i in range(2, x//2 + 1):
            if x % i == 0: return False
        return True
    return False

from itertools import product
cnt = 0
for x in product('01234567', repeat=5):
    s = ''.join(x)
    flag = False
    if s[0] != '0':
        for i in range(len(s) - 1):
            for j in range(i, len(s)):
                if s[i] != s[j] and p(int(s[i]) + int(s[j])):
                    flag = True
                    break
    if flag:
        cnt += 1
print(cnt)


"""№2"""
from itertools import product
cnt = 0
for x in product('!*!*Ш*В!!', repeat=5):
    s = ''.join(x)
    if '*Ш' not in s and 'Ш*' not in s and 'ВШ' not in s and 'ШВ' not in s:
        cnt += 1
print(cnt)


"""№3"""
from itertools import permutations
cnt = 0
for x in set(''.join(x) for x in permutations('АММИАКАТ', r=8)):
    if any(i in x for i in set(''.join(i) for i in permutations('АИАА', r=2)))\
            or any(j in x for j in set(''.join(j) for j in permutations('ММКТ', r=2))):
        cnt += 1
print(cnt)


"""№4"""
n = [int(x) for x in open('v2-17-1.txt')]

ma = -1000000000
for x in n:
    if abs(x) % 10 == 1:
        ma = max(ma, x)

kp = 0
mas = -1000000000
for i in range(len(n) - 1):
    if (abs(min(n[i], n[i + 1])) % 10 == 4) and (n[i]**2 + n[i + 1]**2 < ma**2):
        kp += 1
        mas = max(mas, n[i]**2 + n[i + 1]**2)
print(kp, mas)


"""№5"""
def p(x):
    xn = ''
    while x > 0:
        xn = str(x % 5) + xn
        x //= 5
    return xn == xn[::-1]

n = [int(x) for x in open('v1-17-2.txt')]

k17 = []
for x in n:
    if x % 17 != 0:
        k17.append(x)
med = sum(k17)/len(k17)

kt = 0
ma = -1000000000
for i in range(len(n) - 2):
    tr = [n[i], n[i + 1], n[i + 2]]
    if p(sum(tr)) and max(tr) < med:
        kt += 1
        ma = max(ma, sum(tr))
print(kt, ma)
