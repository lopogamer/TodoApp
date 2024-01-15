from tkinter import *

# Functions
def add():
    listbox.insert("end", entry.get())
    entry.delete(0, "end")

def delete():
    listbox.delete("anchor")

def clear():
    listbox.delete(0, "end")

def save():
    with open("todo.txt", "w") as f:
        for i in range(listbox.size()):
            f.write(listbox.get(i) + "\n")

def load():
    with open("todo.txt", "r") as f:
        for line in f:
            listbox.insert("end", line.strip())
def markascomplete():
    selected_index = listbox.curselection()

    if selected_index:
        # get the task text
        task_text = listbox.get(selected_index[0])

        # check if the task is already marked as completed
        if task_text.startswith("✔"):
            # change the text color to black
            listbox.itemconfig(selected_index[0], fg="black")

            # Remove the checkmark from the task
            unchecked_item = task_text[2:]
            listbox.delete(selected_index[0])
            listbox.insert(selected_index[0], unchecked_item)
        else:
            # change the text color to green
            listbox.itemconfig(selected_index[0], fg="green")

            # insert a checkmark at the beginning of the task
            checked_task = "✔ " + task_text
            listbox.delete(selected_index[0])
            listbox.insert(selected_index[0], checked_task)


def about():
    about_text = (
        "TODO App\n\n"
        "Version 1.0\n\n"
        "Made by: Luan Ribeiro\n\n"
        "2024\n\n"
        "This app was made using Python and Tkinter.\n\n"
        "github.com/lopogamer\n\n"
        
    )
    
    abbout_window = Toplevel(root)
    abbout_window.title("About")
    abbout_window.geometry("500x400")
    abbout_window.resizable(False, False)

    #adding scrollbar
    scrollbar = Scrollbar(abbout_window, orient=VERTICAL)
    scrollbar.pack(side=RIGHT, fill=Y)
    # Creating Text Widget
    about_textbox = Text(
        abbout_window,
        font=("Arial", 12),
        wrap="word",  # wrap text at full words only
        yscrollcommand=scrollbar.set,  # the scrollbar should control the y-axis of the Text
    )
    about_textbox.pack(fill="both", expand=True, padx=10, pady=10) # fill the window and expand with window
    
    # Inserting text into the Text widget
    about_textbox.insert("1.0", about_text)
    scrollbar.config(command=about_textbox.yview)

def help():
    help_text = (
        "Welcome to the TODO App!\n\n"
        "This app allows you to keep track of your tasks.\n\n"
        "To add a task, type it into the entry box and click the 'Add' button.\n\n"
        "To delete a task, select it in the listbox and click the 'Delete' button.\n\n"
        "To mark a task as completed, select it in the listbox and click the 'Mark as completed' button.\n\n"
        "To clear the listbox, click the 'Clear' button.\n\n"
        "To save the listbox, click the 'Save' button.\n\n"
        "To load the listbox, click the 'Load' button.\n\n"
        "To exit the app, click the 'Exit' button.\n\n"
        "To learn more about the app, click the 'About' button.\n\n"
        "To get help, click the 'Help' button.\n\n"
        
    )

    help_window = Toplevel(root)
    help_window.title("Help")
    help_window.geometry("500x400")
    help_window.resizable(False, False)

    #adding scrollbar
    scrollbar = Scrollbar(help_window, orient=VERTICAL)
    scrollbar.pack(side=RIGHT, fill=Y)
    # Creating Text Widget
    help_textbox = Text(
        help_window,
        font=("Arial", 12),
        wrap="word",  # wrap text at full words only
        yscrollcommand=scrollbar.set,  # the scrollbar should control the y-axis of the Text
    )
    help_textbox.pack(fill="both", expand=True, padx=10, pady=10) # fill the window and expand with window

    # Inserting text into the Text widget
    help_textbox.insert("1.0", help_text)

    # Configure the scrollbar
    scrollbar.config(command=help_textbox.yview)

# Creating Window
root = Tk()
root.title("TODO App")
root.geometry("650x650")
root.resizable(False, False)
root.config(bg="#fff")

# Creating Title
title = Label(root, text="TODO App", font=("Arial", 30, "bold"), bg="#fff")
title.pack(pady=10)

# Creating Entry
entry = Entry(root, font=("Arial", 20), bg="#fff")
entry.pack(pady=10)

# Creating Button
button = Button(root, text="Add", font=("Arial", 20), bg="#fff", command=add)
button.pack(pady=10)

# Creating Delete Button
delete_button = Button(root, text="Delete", font=("Arial", 20), bg="#fff", command=delete)
delete_button.pack(pady=10)

# Creating a mark as completed button
mark_button = Button(root, text="Mark as completed", font=("Arial", 20), bg="#fff", command = markascomplete)
mark_button.pack(pady=10)

# Creating Listbox
listbox = Listbox(root, font=("Arial", 20), bg="#fff", width=25, height=10)
listbox.pack(pady=10)



# Creating Menu
menu = Menu(root)
root.config(menu=menu)

# Creating File Menu
file_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="File", menu=file_menu)

# Adding File Menu Items
file_menu.add_command(label="Clear", command=clear)
file_menu.add_command(label="Save", command=save)
file_menu.add_command(label="Load", command=load)
file_menu.add_command(label="Exit", command=root.quit)

# Creating Help Menu
help_menu = Menu(menu, tearoff=False)
menu.add_cascade(label="Help", menu=help_menu)

# Adding Help Menu Items
help_menu.add_command(label="About", command=about)
help_menu.add_command(label="Help", command=help)

# Running
root.mainloop()
