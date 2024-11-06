import json

import json.scanner

with open(file="data.json", mode="r", newline="") as json_file:
    data = json.load(json_file)
    json_file.close()
students: dict = data

print(students)