# List - Mutable, ordered, duplicate values

player_list = ['Maradona','Pele',' Ronaldo','Steffi','Maradona']
print(player_list)
player_list.append('Martina Hingis')
player_list.remove('Steffi')
print(player_list)


# Tuple - immutable,ordered, duplicate values, no new items can be added / removed
player_list = ('Maradona','Pele',' Ronaldo','Steffi','Maradona')
print(player_list)

#Set - unordered, no duplication, set items are frozen, new items can be added and removed
player_list = {'Maradona','Pele',' Ronaldo','Steffi','Maradona'}
player_list.add('Stephen Edberg')
player_list.remove('Pele')

print(player_list)

