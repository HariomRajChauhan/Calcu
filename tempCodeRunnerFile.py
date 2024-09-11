from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import os

def add_image(frame, normal_path, clicked_path, col=0, command=None):
    # Load normal and clicked images
    normal_image = Image.open(normal_path).resize((90, 65))
    clicked_image = Image.open(clicked_path).resize((90, 65))

    tk_normal_image = ImageTk.PhotoImage(normal_image)
    tk_clicked_image = ImageTk.PhotoImage(clicked_image)

    # Create a label for the image
    image_label = Label(frame, image=tk_normal_image, padx=0, pady=0, borderwidth=0, highlightthickness=0)
    image_label.image = tk_normal_image  # Keep a reference to prevent garbage collection
    image_label.grid(row=0, column=col, sticky=N+S+E+W)

    # Define functions to handle click effect
    def on_click(event):
        image_label.config(image=tk_clicked_image)  # Change to clicked image
        if command:  # Call the actual command function
            command(event)
    
    def on_release(event):
        image_label.config(image=tk_normal_image)  # Change back to normal image
    
    # Bind mouse events for click effect
    image_label.bind("<Button-1>", on_click)  # On mouse press
    image_label.bind("<ButtonRelease-1>", on_release)  # On mouse release

    return image_label

def set_Value(value):
    current_value = display_label.cget("text")
    
    if value == "DEL":
        display_label.config(text=current_value[:-1])
    elif value == "AC":
        display_label.config(text="")
        display_label_down.config(text="")
    elif value == "00":
        display_label.config(text=current_value + "00")
    elif value == "=":
        try:
            result = str(eval(current_value))
            if result.find("."):
                result = str(round(float(result), 8))
            display_label.config(text=current_value)
            display_label_down.config(text="Ans = "+result)
        except NameError:
            display_label.config(text = "")
            display_label_down.config(text="Name Error")
        except ValueError:
            display_label.config(text="")
            display_label_down.config(text="Value Error")
        except ZeroDivisionError:
            display_label.config(text="")
            display_label_down.config(text="Zero Division Error")
        except SyntaxError:
            display_label.config(text="")
            display_label_down.config(text="Syntax Error")
        except Exception as e:
            display_label.config(text="")
            display_label_down.config(text=f"Invalid Input: {e}")
    else:
        display_label.config(text=current_value + value)

root = Tk()
root.title("Calculator")
root.geometry("360x390")
root.iconbitmap("assets/icon.ico")
root.resizable(False, False)

# Display Frame Here:
Display_frame = Frame(root, width=360, height=65, padx=0, pady=0, borderwidth=0, highlightthickness=0)
Display_frame.grid(row=0, column=0)

display_label = Label(Display_frame, text="", font=("monospace",30), padx=0, pady=0, fg="black", borderwidth=0, highlightthickness=0)
display_label.grid(row=0, column=0)

display_label_down = Label(Display_frame, text="", font=("monospace", 22), padx=0, pady=0, fg="black", borderwidth=0, highlightthickness=0)
display_label_down.grid(row=1, column=0)

# All Buttons Here:
main_frame = Frame(root, bg="black", width=360, height=325, padx=0, pady=0, borderwidth=0, highlightthickness=0)
main_frame.grid(row=1, column=0)

first_frame = Frame(main_frame, bg="black", width=360, height=65, padx=0, pady=0)
first_frame.grid(row=0, column=0)

add_image(first_frame, "assets/exit.png", "assets/exit_clicked.png", 0, lambda e: root.destroy())
add_image(first_frame, "assets/00.png", "assets/00_clicked.png", 1, lambda e: set_Value("00"))
add_image(first_frame, "assets/del.png", "assets/del_clicked.png", 2, lambda e: set_Value("DEL"))
add_image(first_frame, "assets/ac.png", "assets/ac_clicked.png", 3, lambda e: set_Value("AC"))

second_frame = Frame(main_frame, bg="black", width=360, height=65, padx=0, pady=0)
second_frame.grid(row=1, column=0)

add_image(second_frame, "assets/7.png", "assets/7_clicked.png", 0, lambda e: set_Value("7"))
add_image(second_frame, "assets/8.png", "assets/8_clicked.png", 1, lambda e: set_Value("8"))
add_image(second_frame, "assets/9.png", "assets/9_clicked.png", 2, lambda e: set_Value("9"))
add_image(second_frame, "assets/multiple.png", "assets/multiple_clicked.png", 3, lambda e: set_Value("*"))

third_frame = Frame(main_frame, bg="black", width=360, height=65, padx=0, pady=0)
third_frame.grid(row=2, column=0)

add_image(third_frame, "assets/4.png", "assets/4_clicked.png", 0, lambda e: set_Value("4"))
add_image(third_frame, "assets/5.png", "assets/5_clicked.png", 1, lambda e: set_Value("5"))
add_image(third_frame, "assets/6.png", "assets/6_clicked.png", 2, lambda e: set_Value("6"))
add_image(third_frame, "assets/divide.png", "assets/divide_clicked.png", 3, lambda e: set_Value("/"))

fourth_frame = Frame(main_frame, bg="black", width=360, height=65, padx=0, pady=0)
fourth_frame.grid(row=3, column=0)

add_image(fourth_frame, "assets/1.png", "assets/1_clicked.png", 0, lambda e: set_Value("1"))
add_image(fourth_frame, "assets/2.png", "assets/2_clicked.png", 1, lambda e: set_Value("2"))
add_image(fourth_frame, "assets/3.png", "assets/3_clicked.png", 2, lambda e: set_Value("3"))
add_image(fourth_frame, "assets/minus.png", "assets/minus_clicked.png", 3, lambda e: set_Value("-"))

fifth_frame = Frame(main_frame, bg="black", width=360, height=65, padx=0, pady=0)
fifth_frame.grid(row=4, column=0)

add_image(fifth_frame, "assets/0.png", "assets/0_clicked.png", 0, lambda e: set_Value("0"))
add_image(fifth_frame, "assets/dot.png", "assets/dot_clicked.png", 1, lambda e: set_Value("."))
add_image(fifth_frame, "assets/equal.png", "assets/equal_clicked.png", 2, lambda e: set_Value("="))
add_image(fifth_frame, "assets/add.png", "assets/add_clicked.png", 3, lambda e: set_Value("+"))

root.mainloop()
