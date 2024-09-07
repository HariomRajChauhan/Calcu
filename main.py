from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter import simpledialog
from PIL import ImageTk, Image
import os

# Functions Here:

def add_image(frame, image_path, col=0, command=None):
    image = Image.open(image_path)
    image = image.resize((90, 65))
    tk_image = ImageTk.PhotoImage(image)
    image_label = Label(frame, image=tk_image)
    image_label.image = tk_image
    image_label.grid(row=0, column=col, )
    if command:
        image_label.bind("<Button-1>", command)
    return image_label

def set_Value(value):
    current_value = display_label.cget("text")
    
    if value == "DEL":
        # Delete the last character
        display_label.config(text=current_value[:-1])
    elif value == "AC":
        # Clear all content
        display_label.config(text="")
    elif value == "00":
        # Add double zero
        display_label.config(text=current_value + "00")
    elif value == "=":
        # Evaluate the expression
        try:
            # Evaluate the current expression safely
            result = str(eval(current_value))
            if result.find("."):
                result = str(round(float(result), 8))

            # Display the result
            display_label.config(text=result)
        except NameError:
            # Handle invalid names
            messagebox.showerror("Error", "Invalid Name")
            display_label.config(text="")
        except ValueError:
            # Handle invalid values
            messagebox.showerror("Error", "Invalid Value")
            display_label.config(text="")
        except ZeroDivisionError:
            # Handle division by zero error
            messagebox.showerror("Error", "Cannot divide by zero")
            display_label.config(text="")
        except SyntaxError:
            # Handle syntax errors (e.g., incomplete expressions)
            messagebox.showerror("Error", "Invalid Syntax")
            display_label.config(text="")
        except Exception as e:
            # Handle any other exceptions
            messagebox.showerror("Error", f"Invalid Input: {e}")
            display_label.config(text="")
    else:
        # Append the number or operator to the display
        display_label.config(text=current_value + value)

root = Tk()
root.title("Calculator")
root.geometry("376x410")
root.iconbitmap("assets/icon.ico")
root.resizable(False, False)

# Display Frame Here:
Display_frame = Frame(root, bg="yellow", width=360, height=65)
Display_frame.grid(row=0, column=0)

display_label = Label(Display_frame, text="", font=("monospace", 40),padx=0,pady=0, bg="yellow", fg="black")
display_label.grid(row=0, column=0)

# All Buttons Here:
main_frame = Frame(root, bg="black", width=360, height=325)
main_frame.grid(row=1, column=0)

first_frame = Frame(main_frame, bg="black", width=360, height=65)
first_frame.grid(row=0, column=0)

add_image(first_frame, "assets/exit.png", 0, lambda e: root.destroy())
add_image(first_frame, "assets/00.png", 1, lambda e: set_Value("00"))
add_image(first_frame, "assets/del.png", 2, lambda e: set_Value("DEL"))
add_image(first_frame, "assets/ac.png", 3, lambda e: set_Value("AC"))

second_frame = Frame(main_frame, bg="black", width=360, height=65)
second_frame.grid(row=1, column=0)

add_image(second_frame, "assets/7.png", 0, lambda e: set_Value("7"))
add_image(second_frame, "assets/8.png", 1, lambda e: set_Value("8"))
add_image(second_frame, "assets/9.png", 2, lambda e: set_Value("9"))
add_image(second_frame, "assets/multiple.png", 3, lambda e: set_Value("*"))

third_frame = Frame(main_frame, bg="black", width=360, height=65)
third_frame.grid(row=2, column=0)

add_image(third_frame, "assets/4.png", 0, lambda e: set_Value("4"))
add_image(third_frame, "assets/5.png", 1, lambda e: set_Value("5"))
add_image(third_frame, "assets/6.png", 2, lambda e: set_Value("6"))
add_image(third_frame, "assets/divide.png", 3, lambda e: set_Value("/"))

fourth_frame = Frame(main_frame, bg="black", width=360, height=65)
fourth_frame.grid(row=3, column=0)

add_image(fourth_frame, "assets/1.png", 0, lambda e: set_Value("1"))
add_image(fourth_frame, "assets/2.png", 1, lambda e: set_Value("2"))
add_image(fourth_frame, "assets/3.png", 2, lambda e: set_Value("3"))
add_image(fourth_frame, "assets/minus.png", 3, lambda e: set_Value("-"))

fifth_frame = Frame(main_frame, bg="black", width=360, height=65)
fifth_frame.grid(row=4, column=0)

add_image(fifth_frame, "assets/0.png", 0, lambda e: set_Value("0"))
add_image(fifth_frame, "assets/dot.png", 1, lambda e: set_Value("."))
add_image(fifth_frame, "assets/equal.png", 2, lambda e: set_Value("="))
add_image(fifth_frame, "assets/add.png", 3, lambda e: set_Value("+"))

root.mainloop()
