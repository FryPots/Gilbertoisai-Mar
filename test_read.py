def listify(text, c):
    out = ""
    return_list = []
    for i in (text):
        if i == c:
            return_list.append(out)
            out = ""
        else:
            out = out + i
    return return_list

f = open("list_save.txt", "r")
print(listify(f.read(), "\n"))
