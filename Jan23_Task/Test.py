# Please read this first before considering this as a valid code
# Hi Sir ,This class has been created to Just test the functionality that has been developed inside the helper classes
# Please dont consider the print statments which have been written inside it


# from krishna_dict.krish_dichelper import dicmethods
# d={'key1':'value1','key2':'value2'}
# d1=dicmethods(d)
# print(d1.getkeys())
# print(d1.getvalues())
# print(d1.getvalueforkey('key1'))


# from krishna_list.krish_listhelper import lismethods
# l=[1,2,3,4,5]
# l1=lismethods(l)
# print(l1.revlist())
# print(l1.comblists([6,7,8,9]))
# print(l1.extendlist([78,79,80]))
# print(l1.geteleforanIndex(6))
# print(l1.listsize())
# print(l1.popelement(8))


from krishna_set.krish_sethelper import setmethods
# s={1,2,3,4,5,6}
# s1=setmethods(s)
# print(s1.myset())
# print(s1.unionmynewset({5,6,6,7,8,9}))
# print(s1.findsymdiff({5,6,7}))
# print(s1.discardelefrommyset(9))
# print(s1.popmyset())
# print(s1.myset())
# print(s1.ismysetsubset({2,3,4,5,7,888,8}))

from krishna_tuple.krish_tuplehelper import tupleMethods

t = (1, 2, 3, 4, 5)
t1 = tupleMethods(t)
print(t1.mytuple())
t1.tuplength()
t1.getindxformyval(4)
t1.nooftimeelpresentintuple(6)
t1.addnewelementsintuple([100, 10, 102, 103])
