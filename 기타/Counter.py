from collections import Counter

e_list = ['red', 'blue', 'green', 'red', 'blue', 'yellow']
e_tuple = tuple(e_list)

list_cnt = Counter(e_list)
tuple_cnt = Counter(e_tuple)

print('red:', list_cnt['red'], tuple_cnt['red'])
print('blue:', list_cnt['blue'], tuple_cnt['blue'])

print(dict(list_cnt))
print(dict(tuple_cnt))
