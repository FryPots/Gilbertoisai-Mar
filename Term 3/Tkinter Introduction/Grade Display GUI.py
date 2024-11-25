import tkinter

options = {"O": "Outstanding",
           "A": "Very Good",
           "B": "Good",
           "C": "Average",
           "F": "Fail"}

def display_grade():
    user_input = box_entry.get().upper()

    if user_input in options:
        comment_label.config(text=options[user_input])
    else:
        comment_label.config(text="Error, Invalid Grade")
    
window = tkinter.Tk()
window.title("OMG!")
window.geometry("400x400")

grade: str = ""

box_label = tkinter.Label(master=window,
                          text="Type in your Grade:").pack()

box_entry = tkinter.Entry(master=window,
                          textvariable=grade,
                          width=15)
box_entry.pack()

for i in options:
    button = tkinter.Radiobutton(master=window, text=i)
    button.pack()

comment_label = tkinter.Label(master=window,
                              text="")
comment_label.pack()

window.mainloop()