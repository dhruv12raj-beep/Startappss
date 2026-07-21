'''Move a recently accessed item to the end using OrderedDict.'''

from collections import OrderedDict

od = OrderedDict()
od["a"]= 1
od["b"]= 2
od["c"]= 3
od["d"]= 4

print(od)

print(od["b"])

od.move_to_end("b")
print(od)