# file access modes - r,w,a,c

# data_file = open("data.txt")
# print(data_file)
# print(data_file.read())

# print(data_file.readline())
# print(data_file.readline())

# for line in data_file:
#     print(line)

# with open("data.txt","a") as data_file:
#     data_file.write("\n New line appended here")
#     data_file.close()
#
# data_file = open("data.txt")
# print(data_file.read())

with open("data.txt","w") as data_file:
    data_file.write("New line appended here")
    data_file.close()


