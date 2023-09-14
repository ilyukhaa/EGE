"""№1"""
def isPrime(x):
    if x > 1:
        for i in range(2, x//2 + 1):
            if x % i == 0: return False
        return True
    return False

from itertools import product
cnt = 0
for x in product('0123456', repeat=5):
    k = su = 0
    for n in x:
        su += int(n)
        if int(n) % 2 == 0:
            k += 1
    if x[0] != '0' and k >= 3 and isPrime(su):
        cnt += 1
print(cnt)


"""№2"""
from itertools import product
cnt = 0
for x in product('!*!*Ш*!!!', repeat=5):
    s = ''.join(x)
    if (s.count('*') > s.count('!') + s.count('Ш')) and ('*Ш' not in s) and ('Ш*' not in s):
        cnt += 1
print(cnt)


"""№3"""
from itertools import permutations
cnt = 0
for w in set(''.join(x) for x in permutations('АКАРИДА', r=7)):
    if ('АА' not in w) and ('АИ' not in w) and ('ИА' not in w):
        if all(s not in w for s in set(''.join(i) for i in permutations('КРД', r=2))):
            cnt += 1
print(cnt)


"""№4"""
n = [int(x) for x in open('v3-17-1.txt')]
ma = -1000000000

for x in n:
    if abs(x) % 10 == 5:
        ma = max(ma, x)

kp = 0
mi = 1000000000
for i in range(len(n) - 1):
    if (abs(n[i]) % 10 == 8 or abs(n[i + 1]) % 10 == 8) and not(abs(n[i]) % 10 == 8 and abs(n[i + 1]) % 10 == 8):
        if n[i]**2 + n[i + 1]**2 > ma**2:
            kp += 1
            mi = min(mi, n[i]**2 + n[i + 1]**2)
print(kp, mi)


"""№5"""
def p(x):
    xn = ''
    while x > 0:
        xn = str(x % 5) + xn
        x //= 5
    return xn == xn[::-1]

n = [int(x) for x in open('v3-17-2.txt')]

k31 = []
for x in n:
    if x % 31 == 0:
        k31.append(x)
med = sum(k31)/len(k31)

kt = 0
mi = 1000000000
for i in range(len(n) - 2):
    tr = [n[i], n[i + 1], n[i + 2]]
    if p(sum(tr)) and (sum(tr)/3) > med:
        kt += 1
        mi = min(mi, sum(tr))
print(kt, mi)
