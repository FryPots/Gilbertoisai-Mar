data : str = "FirstName,LastName,PhoneNumber,EmailAddress,John,Doe,123-456-7890,john.doe@example.com,Jane,Smith,987-654-3210,jane.smith@example.com,Alice,Johnson,555-123-4567,alice.johnson@example.com,Bob,Brown,444-987-6543,bob.brown@example.com"

clients: dict = {
    "FirstName"     :   "John",
    "LastName"      :   "Doe",
    "PhoneNumber"   :   "123-456-7890",
    "EmailAddress"  :   "Example@Example.com",
}

def read_csv(csv: str):
    out : list
    for c in csv:
        if c == ",":
            out.append(c)
        


print(clients)