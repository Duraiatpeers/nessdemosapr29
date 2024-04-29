
player_list = ['Maradona','Pele','Ronaldo','Steffi','Maradona']

# # indexing
# print(player_list[0])
#
# # slicing
# # print(player_list[1:3]) # from index - to index - 1
# print(player_list[1:]) # from index - to index - 1
#
# print(player_list[-3:-1]) # from index - to index - 1
#     # -3 to -1-1 ==> -3,-2
#
# print(player_list[-3:]) # from index - to index - 1
#     # -3 to -1-1 ==> -3,-2
#
# print(player_list)

# list comprehension
new_player = [player for player in player_list if player == 'Maradona']
print(new_player)
# player_list.sort()
# print(player_list)
print(sorted(player_list,reverse=True))

# Dict
emp = {
    "empid": "e291",
    "empname": 'Sam',
    "emploc":"Prague"
}

print(emp)

emp["designation"] = "manager"

print(emp)

print(emp.keys())

for key in emp.keys():
    print(emp[key])

emp.pop("emploc")

print(emp)
