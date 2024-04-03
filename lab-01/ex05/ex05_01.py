import itertools

# List ban đầu
my_list = [1, 2, 3]

# Sử dụng permutations() để lấy tất cả các hoán vị của list
permutations_list = list(itertools.permutations(my_list))

# In tất cả các hoán vị
for permutation in permutations_list:
    print(permutation)
