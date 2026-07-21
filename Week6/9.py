'''Combine three dictionaries using ChainMap.
Priority
User
↓
Company
↓
System
'''
from collections import ChainMap

user = {"dhruv": "employee"}
company = {"startappss"}
system = {"python developer"}

cm = ChainMap(user,company,system)

print(cm)
