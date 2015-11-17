# Hash Tables

def hashing_from_two_arrays(keys, values):
  hash_table = {k:v for k, v in zip(keys, values)}
  return hash_table

keys = ['a', 'b', 'c']
values = [1, 2, 3]
hash_t = hashing_from_two_arrays(keys, values)
print hash_t

print map(hash, [0, 1, 2, 3])
print hash(1)
print map(hash, ['a', '1', '2'])
print hash('a')
