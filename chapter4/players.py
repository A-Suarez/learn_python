players = ['ale', 'morandi', 'eryk', 'brett','wallack']
print(players[1:4])

# Omit the first index of the slice
print(players[:3])

# Omit the last index of the slice
print(players[2:])

print("Here are the first three players on my team")
for player in players[:3]:
    print(player.title())