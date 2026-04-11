guest_list = ['Brett', 'Morandi', 'Ryk', 'Wallack']
# Invite statments
brett_msg = f"{guest_list[0]} lives in Strewsberry"
mo_msg = f'{guest_list[1]} is a tweak'
ryk_msg = f'{guest_list[2]} is in Dallas.'
wallack_msg = f'{guest_list[3]} is M.I.A'
print(brett_msg)
print(mo_msg)
print(ryk_msg)
print(wallack_msg)

GM = 'GM'
guest_list.append(GM) 
print(f'The only one that cannot make it is {guest_list[3]}.')

guest_list.remove('Wallack')

print(f'The new guest list is {guest_list}')
print(f'I am inviting {guest_list[0]} , {guest_list[1]}, {guest_list[2]}, {guest_list[3]}')

CORINNE = 'Corinne'
KIM = 'KIM'

guest_list.insert(0, CORINNE)
guest_list.insert(2, KIM)

print(f'I found a bigger table and the larger guest list is the following: {guest_list}')
print(f'Sorry {guest_list[0]} and {guest_list[2]}. You are no longer invited!')

remove_c = guest_list.pop(0)
remove_k = guest_list.pop(1)

uninvited_list = [remove_c, remove_k]

print(f'The uninvited list is the following: {uninvited_list}.')

del guest_list[0]
del guest_list[1]
del guest_list[0]
del guest_list[0]

print(f'Empty list: {guest_list}')