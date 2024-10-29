file = open("clients.csv", "a")
file.close()

file = open("clients.csv", "r").read()

clients : dict = {
    "FirstName"     :   "John",
    "LastName"      :   "Doe",
    "PhoneNumber"   :   "123-456-7890",
    "EmailAddress"  :   "Example@Example.com",
}

def import_csv(csv):
    tmp = ""
    out = []
    for c in csv:
        match c:
            case ",":
                out.append(tmp)
                tmp = ""
            case _:
                tmp += c
    return out

client_csv = import_csv(file)

for i in range( 0, len(client_csv), len(clients)):
    print(i)
print(len(client_csv))