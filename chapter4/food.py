my_foods = ['colombian', 'chinese', 'japanese', 'chicken cutlet']

# copying a list
friend_foods = my_foods[:]
print(friend_foods)

# appending a copied list
my_foods.append('burgers')
friend_foods.append('bbq')

print(f'My favorite foods are {my_foods}!')

print(f'My friends favorite foods are {friend_foods}!')

for food in my_foods[1:4]:
    print(food.title())

