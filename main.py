from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Scribbled Canvas")
root.geometry("1000x600")
canvas = Canvas(width=1000, height=400, bg="white",
                highlightbackground="black")
canvas.pack()
label = Label(text="Choose Color=>")
label.place(relx=0.6, rely=0.95, anchor=CENTER)

fillcolour=["red","orange","yellow","green","blue","black","pink","grey"]
coordinate_values = [1,2,5,10,20,50,100,200,300,400,500,600,700,800,900,1000]

colourDropdown = ttk.Combobox(root,state="readonly",values=fillcolour,width=10)
colourDropdown.place(relx=0.7,rely=0.95,anchor=CENTER)

Lstartx = Label(root,text="startx: ")
Lstartx.place(relx=0.1,rely=0.9,anchor=CENTER)
startxdrop = ttk.Combobox(root,state="readonly",values=coordinate_values,width=10)
startxdrop.place(relx=0.2,rely=0.9,anchor=CENTER)

Lstarty = Label(root,text="starty: ")
Lstarty.place(relx=0.3,rely=0.9,anchor=CENTER)
startydrop = ttk.Combobox(root,state="readonly",values=coordinate_values,width=10)
startydrop.place(relx=0.4,rely=0.9,anchor=CENTER)

Lendx = Label(root,text="endx: ")
Lendx.place(relx=0.5,rely=0.9,anchor=CENTER)
endxdrop = ttk.Combobox(root,state="readonly",values=coordinate_values,width=10)
endxdrop.place(relx=0.6,rely=0.9,anchor=CENTER)

Lendy = Label(root,text="endy: ")
Lendy.place(relx=0.7,rely=0.9,anchor=CENTER)
endydrop = ttk.Combobox(root,state="readonly",values=coordinate_values,width=10)
endydrop.place(relx=0.8,rely=0.9,anchor=CENTER)

def circle(event):
    oldx = startxdrop.get()
    oldy = startydrop.get()
    newx = endxdrop.get()
    newy = endydrop.get()
    keypress = "c"
    draw(keypress,oldx,oldy,newx,newy)
def rectangle(event):
    oldx = startxdrop.get()
    oldy = startydrop.get()
    newx = endxdrop.get()
    newy = endydrop.get()
    keypress = "r"
    draw(keypress,oldx,oldy,newx,newy)
def line(event):
    oldx = startxdrop.get()
    oldy = startydrop.get()
    newx = endxdrop.get()
    newy = endydrop.get()
    keypress = "l"
    draw(keypress,oldx,oldy,newx,newy)
def draw(keypress, oldx,oldy,newx,newy):
    colour = colourDropdown.get()
    if keypress == "c":
        canvas.create_oval(oldx,oldy,newx,newy,width = 3,fill = colour)
    if keypress == "r":
        canvas.create_rectangle(oldx,oldy,newx,newy,width = 3,fill = colour)
    if keypress == "l":
        canvas.create_line(oldx,oldy,newx,newy,width = 3,fill = colour)
root.bind("<c>",circle)
root.bind("<r>",rectangle)
root.bind("<l>",line)
root.mainloop()
