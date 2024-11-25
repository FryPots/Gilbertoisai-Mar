import tkinter
import string

characters = string.ascii_lowercase
char_dict: dict = {}
new_dict = {}
for i in characters:
    char_dict[i] = 0
char_dict["other"] = 0

root = tkinter.Tk()
root.title("• Character Ocurrence Counter")
root.geometry("1500x1500")

entry_string = tkinter.StringVar()
reult_label = tkinter.StringVar()

title_label = tkinter.Label(master=root, text="Enter a message:").pack()
message_entry = tkinter.Entry(master=root, textvariable=entry_string)
message_entry.pack(pady=15)

def analyze_string():
    string_test = entry_string.get().casefold()
    new_dict = char_dict.copy()
    print(string_test)
    for c in string_test:
        if c in new_dict:
            new_dict[c] += 1
        else:
            new_dict["other"] += 1
    result.config(text=str(new_dict))
button = tkinter.Button(master=root, text="Count Occurrences", command=analyze_string)
button.pack()
result = tkinter.Label(master=root)
result.pack()


root.mainloop()