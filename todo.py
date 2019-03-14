from tkinter import *
import random
#Creating the root window
root = Tk()

#Change root window title
root.title("My Super To Do List")

#Change background color of Window
root.configure(bg="white")

#Change the Size of the window
root.geometry("300x275")

#Creating an empty list
tasks =[]

#Creating default list
tasks = ["Call mom", "Buy a Guitar", "Take a nap"]

#Creating Functions

#Update the listbox
def update_listbox():
    #Clearing the listbox
    clear_listbox()
    #Populate the listbox
    for task in tasks:
        lb_tasks.insert("end",task)

def clear_listbox():
    lb_tasks.delete(0,"end")

def add_task():
    #Get the task to add
    task = lbl_input.get()
    #Make Sure the task is not empty
    if (task != ""):
        #Add the task to the listbox
        tasks.append(task)
        #Update the listbox
        update_listbox()

    else:
        lbl_display["text"] = "Please enter a task:"
    lbl_input.delete(0,"end")

def del_all():
    #Since we are chnging the list , we need to globalize the list
    global tasks
    #Clear the tasks list
    tasks = []
    #Update the listbox
    update_listbox()

def del_one():
    #Get the selected task
    task = lb_tasks.get("active")
    #Confirm it is in listbox
    if (task in tasks):
        tasks.remove(task)
    #Update the listbox
    update_listbox()

def sort_asc():
    #Sort the list
    tasks.sort()
    #Update the listbox
    update_listbox()

def sort_desc():
    #Sort the list
    tasks.sort()
    #reverse the list
    tasks.reverse()
    #Update the listbox
    update_listbox()

def choose_random():
    #Choosing the random task
    task = random.choice(tasks)
    #Display the random task
    lbl_display["text"] = task

def number_of_tasks():
    #Get the number of tasks
    number_of_task = len(tasks)
    #Format the message
    msg = "Number of Tasks: %s"%(number_of_task)
    #Display the total number of tasks
    lbl_display["text"] = msg


#Creating buttons
lbl_txt = Label(root, text="To-do-list", bg="white")
lbl_txt.grid(row=0,column=0)

lbl_display = Label(root, text="", bg="white")
lbl_display.grid(row=0,column=1)

lbl_input = Entry(root, width=15)
lbl_input.grid(row=1,column=1)

btn_add_task = Button(root, text="Add Task", command=add_task, bg="white", fg="green")
btn_add_task.grid(row=1,column=0)

btn_del_all = Button(root, text="Delete All Tasks", command=del_all, bg="white", fg="green")
btn_del_all.grid(row=2,column=0)

btn_del_one = Button(root, text="Delete", command=del_one, bg="white", fg="green")
btn_del_one.grid(row=3,column=0)

btn_sort_asc = Button(root, text="Ascending Sort", command=sort_asc, bg="white", fg="green")
btn_sort_asc.grid(row=4,column=0)

btn_sort_desc = Button(root, text="Sort(DESC)", command=sort_desc, bg="white", fg="green")
btn_sort_desc.grid(row=5,column=0)

btn_choose_random = Button(root, text="Choose Random", command=choose_random, bg="white", fg="green")
btn_choose_random.grid(row=6,column=0)

btn_number_of_tasks = Button(root, text="Number of Tasks", command=number_of_tasks, bg="white", fg="green")
btn_number_of_tasks.grid(row=7,column=0)

btn_exit = Button(root, text="Exit", command=exit, bg="white", fg="green")
btn_exit.grid(row=8,column=0)

#Creating the listbox
lb_tasks = Listbox(root)
lb_tasks.grid(row=2,column=1, rowspan=7)

#Calling the root window
root.mainloop()