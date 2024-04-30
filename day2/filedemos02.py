import os

if(os.path.exists("C:\\Users\\d.duraivelan\\PycharmProjects\\nessproject\\day2\\data1.txt")):
    print('File exists')
    os.remove("data1.txt")
else:
    print("Data file doesn't exists")

print(os.listdir())
