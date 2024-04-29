num1 = 100
num2 = 200
num3 = 300

if num1 > 1000:
    print('num1 is the biggest number')
    if(True):
        print('True')
elif num1 > num3:
    print('num1 is bigger than num3')
elif num1 > num2:
    print('num1 is bigger than num2')
else:
    print('num1 is the least number')


player_list = ['Gabriela Sabatini','Chris Evert', 'Monica Seles','Ivan lendl'];
# for player in player_list:
#     print(player)

print(len(player_list))

# count = 0;
# while count < len(player_list):
#     print(player_list[count])
#     count += 1


# break - this will exit the loop
# continue - this will exit current iteration and continue with next iteration

# count = 0;
# while count < len(player_list):
#     print(player_list[count])
#     continue
#     count += 1
