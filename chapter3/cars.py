cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

temp_change = ['bmw', 'audi', 'toyota', 'subaru']
print(f'here is the original order of the list {temp_change}')
print(f'here is the sorted order of the list {sorted(temp_change)}')
print(f'here is the original order again {temp_change}')

print(len(cars))