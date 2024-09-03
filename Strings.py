print("Hello! Welcome")
fullName = input("What is your name?")
line = []

def sep(text, char):
    out = ""
    for i in range(len(text)):
        out += text[i]
        print(out, i)
        if text[i] == char or text[1] == "":
            line.append(out)
            out = ""
            i += 1
            

sep(fullName, " ")
print(line)
input()