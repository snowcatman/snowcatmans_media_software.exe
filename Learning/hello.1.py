import string
from itertools import count
from collections import OrderedDict
s = string.ascii_lowercase
od = OrderedDict()
for count,i in enumerate(s):
    od[count] = i

print()
print(od[7]+od[4]+od[11]+od[11]+od[14]+',')
print('     ', (od[22]+od[14]+od[17]+od[11]+od[3]+'.'))
