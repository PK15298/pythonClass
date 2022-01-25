from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
root=Tk()
root.title("HTML")
root.minsize(650,650)
root.maxsize(650,650)

file = ImageTk.PhotoImage(Image.open("open.png"))
save1 = ImageTk.PhotoImage(Image.open("save.png"))
run1 = ImageTk.PhotoImage(Image.open("exit.jpg"))

labelfile = Label(root,text="File Name")
labelfile.place(relx=0.28,rely=0.03,anchor=CENTER)

inputfile=Entry(root)
inputfile.place(relx=0.46,rely=0.03,anchor=CENTER)

mytext=Text(root,height=35,width=80)
mytext.place(relx=0.05,rely=0.55,anchor=CENTER)
name = ""
def openFile():
    global name
    mytext.delete(1.0, END)
    inputfile.delete(0, END)
    text_file = filedialog.askopenfilename(title=" Open Text File", filetypes=(("Text Files", "*.txt"),))
    print(text_file)
    name = os.path.basename(text_file)
    formated_name = name.split('.')[0]
    inputfile.insert(END,formated_name)
    root.title(formated_name)
    text_file = open(name,'r')
    paragraph=text_file.read()
    mytext.insert(END,paragraph)
    text_file.close()
    
def save():
    input_name = inputfile.get()
    file = open(input_name+".txt", "w")
    data = mytext.get("1.0",END)
    print(data)
    file.write(data)
    inputfile.delete(0, END)
    mytext.delete(1.0, END)
   
    
def closeWindow():
    root.destroy()
    
open_button=Button(root,image=file,text="OpenFile", command=openFile)
open_button.place(relx=0.05,rely=0.03,anchor=CENTER)
save_button=Button(root, image=save1,text="Save File", command=save)
save_button.place(relx=0.11,rely=0.03,anchor= CENTER)
exit_button=Button(root,image=run1,text="Exit File", command=closeWindow)
exit_button.place(relx=0.17,rely=0.03,anchor= CENTER)


root.mainloop()