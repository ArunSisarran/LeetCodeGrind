# A hashmap is a data stucture that stores values and pairs them up
# with a unique identifier called keys.
# Like this key : value

# Benefits of hashmaps:
# Custom keys are easier to work with
# Hashmaps allow for searching in O(1) runtime

# Hashmap keys must be a immutable data type
# If you try and assign a mutable type like an array to a hashmap
# you wil get a type error

# Declaring Hashmaps:
# map = {}
# When doing a hashmap this way you need to first initalize every key
# Ex. map[someVar] = []
# To avoid having to initalize an array for you keys everytime you
# an use a defualtdict which will auto initalize all keys
# from collections import defaultdict
# map = defaultdict(type)

# Hashmap Retriving Functions:
# hashmap.keys() returns all of keys from the hashmap
# hashmap.values() returns all of the values from the hashmap
# hashmap.items() returns all of the key value pairs as tuples
