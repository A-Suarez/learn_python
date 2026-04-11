teams = ['ecuador', 'brazil', 'spain', 'argentina']
print(teams)
print(sorted(teams))
print(teams)

teams.reverse()
print(teams)

teams.sort()
print(teams)

teams.sort(reverse=True)
print(teams)

teams.sort()
print(teams)

fav_team = teams[2]
print(f'My fav team is {fav_team}')

teams.insert(3, 'france')
print(f'The top 5 teams will be {teams}')

fourth_place = teams.pop(2)
print(f'4th place: {fourth_place}')

teams.remove('brazil')
teams.remove('france')
print(f'The final will be: {teams}')

del teams[0]
print(f'The Winner is {teams}')

