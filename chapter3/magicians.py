magicians = ['alice', 'david', 'carolina']
# for magician in magicians:
#     print(magician)

for magician in magicians:
    print(f'{magician.title()}, that was a great trick!')
    print('I am excited for your next trick!')
# No indentation means the end of the Loop
print('Thank you, everyone. That was a great magic show!')

# Common Errors
magicians_error = ['alice', 'david', 'carolina']

for magician in magicians_error:
    print('This will cause an Error')
print(f'{magician.title()}, this will also cause an error')


