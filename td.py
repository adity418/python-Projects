from tkinter import *
import tkinter.messagebox

# Initialize global variables
input_text = ""

def entertask():
    global input_text  # Declare input_text as global
    root1 = Tk()  # Moved creation of root1 outside the add function
    root1.title("Add Task")

    def add():
        global input_text  # Access input_text globally
        input_text = entry_task.get(1.0, "end-1c")  # Use "end-1c" to remove newline character
        if input_text.strip() == "":  # Check if input_text is empty or whitespace
            tkinter.messagebox.showwarning(title="Warning!", message="Please Enter some Text")
        else:
            listBox_task.insert(END, input_text)
            root1.destroy()

    entry_task = Text(root1, width=40, height=4)
    entry_task.pack()
    button_temp = Button(root1, text="Add task", command=add)
    button_temp.pack()
    root1.mainloop()

def deletetask():
    selected = listBox_task.curselection()
    if selected:  # Check if any item is selected
        listBox_task.delete(selected[0])

def markcompleted():
    selected = listBox_task.curselection()
    if selected:  # Check if any item is selected
        index = selected[0]
        task_text = listBox_task.get(index)
        if task_text.endswith(" ✓"):  # If already marked, unmark it
            task_text = task_text[:-2]  # Remove the check mark
        else:
            task_text += " ✓"  # Add a check mark
        listBox_task.delete(index)
        listBox_task.insert(index, task_text)

window = Tk()
window.title("To-Do List APP")

frame_task = Frame(window)
frame_task.pack()

listBox_task = Listbox(frame_task, bg="black", fg="white", height=15, width=50, font="Helvetica")
listBox_task.pack(side=LEFT)

scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=RIGHT, fill=Y)
listBox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listBox_task.yview)

entry_button = Button(window, text="Add task", width=50, command=entertask)
entry_button.pack()

delete_button = Button(window, text="Delete selected task", width=50, command=deletetask)
delete_button.pack(pady=3)

mark_button = Button(window, text="Mark as completed", width=50, command=markcompleted)
mark_button.pack(pady=3)

window.mainloop()
