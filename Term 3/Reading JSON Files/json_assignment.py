import json

def read_json(file_name):
    with open(file=file_name, mode="r", newline="") as json_file:
        data = json.load(json_file)
        json_file.close()
    return data

def convert_json(data):
    dictionary: dict = {}

    for row in data:
        values = data[row]
        keys = values[0]
        for x in keys:
            if x not in dictionary:
                dictionary[x] = []
            dictionary[x].append(keys[x])
    return dictionary

def display_table(students):
    for i in students:
        print(f"""Student ID:     {i}
Name:     |      {students[i]["name"]}
Grade:    |      {students[i]["grade"]}
Group:    |      {students[i]["group"]}
--------------------------------------""")

def main():
    students = read_json("data.json")
    for i in students:
        students[i] = students[i][0]
    display_table(students)
    input()
    main()

if __name__ == "__main__":
    main()