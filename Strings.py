name = input("Insert your full name: ")
line = []

def separate(text, char):
    
    global line
    line = []
    out = ""
    
    for i in range(len(text)):

        if text[i] == " ":
            
            line.append(out)
            out = ""
            
            continue

        out = out + text[i]
    line.append(out)
    
def double(text, each):

    out = ""
    for i in range(len(text)):
        for times in range(each):
            out += text[i]

    return out
while True:

    separate(name, " ")
    fname = line[0]
    fname = fname.capitalize()
    lname = line[1]
    lname = lname.capitalize()
    fullname = fname + " " + lname
    count = len(name) - 1
    dname = double(name, 2)
    dname = dname.capitalize()
    
    
    if len(line) == 2:
        print(f"""Hello {lname}, {fname}! Your name has{count: 04} letters, and your initials are {fname[0]+lname[0]}.
{dname}, your name spelled backwards is {fullname[::-1]}.""")
        input("Enter to exit")

        break
    else:

        print ("Please use only one first and/or last name")
        name = input("Type your name again: ")