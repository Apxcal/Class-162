from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import webbrowser
from tkinter import messagebox
from tkinter import resize

root=Tk()
root.title("HTML IDE")
root.minsize(650, 650)
root.maxsize(650, 650)
root.configure(background="gray")

openimg=ImageTk.PhotoImage(Image.open("open.png"))
saveimg=ImageTk.PhotoImage(Image.open("save.png"))
runimg=ImageTk.PhotoImage(Image.open("runnnn.png"))
run=runimg.resize((15, 15))

label1=Label(root, text="File Name")
label1.place(relx=0.28, rely=0.03, anchor=CENTER)

fileinput=Entry(root)
fileinput.place(relx=0.46, rely=0.03, anchor=CENTER)

areatext=Text(root, height=35, width=80, bg="lightgray", fg="black")
areatext.place(relx=0.5, rely=0.55, anchor=CENTER)

name=""

def openFile():
    global name
    areatext.delete(1.0, END)
    fileinput.delete(0, END)
    htmlfile=filedialog.askopenfilename(title="Open HTML File", filetypes=(("html Files", "*.html"),))
    name=os.path.basename(htmlfile)
    formatted_name=name.split('.')[0]
    fileinput.insert(END, formatted_name)
    root.title(formatted_name)
    htmlfile=open(name, 'r')
    paragraph=htmlfile.read()
    areatext.insert(END, paragraph)
    htmlfile.close()
    
def save():
    filename=fileinput.get()
    openfile=open(filename+".html", 'w')
    texts=areatext.get("1.0", END)
    print(texts)
    openfile.write(texts)
    areatext.delete("1.0", END)
    fileinput.delete("0", END)
    messagebox.showinfo("Update", "Success")
    
def closeWindow():
    root.destroy()
    
    
def run_html_file():
    global name
    global htmlfile
    webbrowser.open_new('file://' + name)
    
runbutton=Button(root, image=runimg, command=run_html_file)
runbutton.place(relx=0.17, rely=0.03, anchor=CENTER)
    
savebutton=Button(root, image=saveimg, command=save)
savebutton.place(relx=0.11, rely=0.03, anchor=CENTER)

openbutton=Button(root, image=openimg, command=openFile)
openbutton.place(relx=0.05, rely=0.03, anchor=CENTER)
    

root.mainloop()