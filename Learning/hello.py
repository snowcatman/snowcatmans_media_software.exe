import string
from itertools import count
from collections import OrderedDict
s = string.ascii_lowercase
ss = string.ascii_uppercase
od = OrderedDict()
ad = OrderedDict()
for count,i in enumerate(s):
    od[count] = i
for count,i in enumerate(ss):
    ad[count] = i



# ---------------------------------------
print()
print('   this is what i want from the new code')
print()
print(ad[7]+od[4]+od[11]+od[11]+od[14]+',')
print(ad[15]+od[17]+od[14]+od[6]+od[0]\
    +od[12]+od[12]+od[12]+od[8]+od[13]+od[6])
print(od[5]+od[14]+od[17])
print(ad[1]+od[4]+od[6]+od[6]+od[8]+od[13]\
    +od[13]+od[4]+od[17]+od[18]+'.')