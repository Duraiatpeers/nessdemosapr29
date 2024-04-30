import json

file_reader = open("data.json")
data = file_reader.read()
json_data = json.loads(data)  # loads - converts json object to python object

# print(json_data)
# print(type(json_data))
#
print(json_data[0])
print(type(json_data[0]))

print(json_data[0]['empname'])
print(type(json_data[0]['empname']))
print(json_data[0]['location'])
print(type(json_data[0]['location']))
print(json_data[0]['salary'])
print(type(json_data[0]['salary']))



# {
#     'empid': 'e001',
#     'empname': 'sam',
#     'designation': 'manager',
#     'location': 'hyderabad'
# }
#

