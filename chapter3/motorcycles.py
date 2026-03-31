motorcycles = ['honda', 'yamha', 'suzuki']
motorcycles[0] = 'test'

print(motorcycles)

# This will append the list
motorcycles_append = ['honda', 'yamha', 'suzuki']
motorcycles_append.append('test')
print(motorcycles_append)

# Here we will build the list one by one
motorcycle_types = []
motorcycle_types.append('honda')
motorcycle_types.append('yamha')
motorcycle_types.append('suzuki')
motorcycle_types.append('test')
motorcycle_types.append('works')
print(motorcycle_types)

# Here I will insert a new value
motorcycle_types.insert(0, 'New Value')
print(motorcycle_types)

