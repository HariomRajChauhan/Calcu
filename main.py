from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
from PIL import ImageTk, Image


def exit():
    result = messagebox.askyesno("Exit", "Are you sure you want to exit?")
    if result:
        root.destroy()
    else:
        pass


def add_image(frame,image_path,col=0,command=None):
    image = Image.open(image_path)
    image = image.resize((90,65))
    tk_image = ImageTk.PhotoImage(image)
    image_label = Label(frame, image=tk_image)
    image_label.image = tk_image
    image_label.grid(row=0, column=col)
    return image_label


root = Tk()
root.title("Calculator")
root.geometry("376x410")
root.iconbitmap("assets/icon.ico")
root.resizable(False, False)

# Display Frame Here :
Display_frame = Frame(root, bg="yellow", width=360, height=65)
Display_frame.grid(row=0, column=0)



# All Buttons Here : 
main_frame = Frame(root,bg="black", width=360, height=325)
main_frame.grid(row=1, column=0)


first_frame = Frame(main_frame, bg="black", width=360, height=65)
first_frame.grid(row=0, column=0)

add_image(first_frame,"assets/exit.png",0)
add_image(first_frame,"assets/00.png",1)
add_image(first_frame,"assets/del.png",2)
add_image(first_frame,"assets/ac.png",3)


second_frame = Frame(main_frame, bg="black", width=360, height=65)
second_frame.grid(row=1, column=0)

add_image(second_frame,"assets/7.png",0)
add_image(second_frame,"assets/8.png",1)
add_image(second_frame,"assets/9.png",2)
add_image(second_frame,"assets/multiple.png",3)

third_frame = Frame(main_frame, bg="black", width=360, height=65)
third_frame.grid(row=2, column=0)

add_image(third_frame,"assets/4.png",0)
add_image(third_frame,"assets/5.png",1)
add_image(third_frame,"assets/6.png",2)
add_image(third_frame,"assets/divide.png",3)

fourth_frame = Frame(main_frame, bg="black", width=360, height=65)
fourth_frame.grid(row=3, column=0)

add_image(fourth_frame,"assets/1.png",0)
add_image(fourth_frame,"assets/2.png",1)
add_image(fourth_frame,"assets/3.png",2)
add_image(fourth_frame,"assets/minus.png",3)

fifth_frame = Frame(main_frame, bg="black", width=360, height=65)
fifth_frame.grid(row=4, column=0)

add_image(fifth_frame,"assets/0.png",0)
add_image(fifth_frame,"assets/dot.png",1)
add_image(fifth_frame,"assets/equal.png",2)
add_image(fifth_frame,"assets/add.png",3)


root.mainloop()

