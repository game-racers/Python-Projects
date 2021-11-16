import time

list1 = list(range(10000))
set1 = set(list1)
fs1 = frozenset(list1)
tup = tuple(list1)
dct = dict()
for i in range(10000):
    dct[str(i)] = str(i)

listStart = time.time()
for i in range(len(list1)):
    i in list1
listEnd = time.time()
print('List took', listEnd - listStart, 'to iterate through every number')

dictStart = time.time()
for i in range(len(dct)):
    i in dct
dictEnd = time.time()
print('Dictionary took', dictEnd - dictStart, 'to iterate through every number')

setStart = time.time()
for i in range(len(set1)):
    i in set1
setEnd = time.time()
print('Set took', setEnd - setStart, 'to iterate through every number')

tupStart = time.time()
for i in range(len(tup)):
    i in tup
tupEnd = time.time()
print('Tuple took', tupEnd - tupStart, 'to iterate through every number')

fsStart = time.time()
for i in range(len(fs1)):
    i in fs1
fsEnd = time.time()
print('Frozenset took', fsEnd - fsStart, 'to iterate through every number')

print("Now to end it")

listStart = time.time()
for j in range(len(list1)):
    del list1[0]
listEnd = time.time()
print('List took', listEnd - listStart, 'to Delete Everything')

dictStart = time.time()
for j in range(len(dct)):
    del dct[str(j)]
dictEnd = time.time()
print('Dictionary took', dictEnd - dictStart, 'to Delete Everything')

setStart = time.time()
for j in range(len(set1)):
    set1.remove(j)
setEnd = time.time()
print('Set took', setEnd - setStart, 'to Delete Everything')

print('Done')
