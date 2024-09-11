# using oops concept

from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image


class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("360x390")
        self.root.iconbitmap("assets/icon.ico")
        self.root.resizable(False, False)
        
        # Create the display frames and labels
        self.create_display()
        # Create all buttons
        self.create_buttons()

    def create_display(self):
        """Creates the display for the calculator."""
        display_frame = Frame(self.root, width=360, height=65, padx=0, pady=0, borderwidth=0, highlightthickness=0)
        display_frame.grid(row=0, column=0)

        self.display_label = Label(display_frame, text="", font=("monospace", 30), padx=0, pady=0, fg="black", borderwidth=0, highlightthickness=0)
        self.display_label.grid(row=0, column=0)

        self.display_label_down = Label(display_frame, text="", font=("monospace", 22), padx=0, pady=0, fg="black", borderwidth=0, highlightthickness=0)
        self.display_label_down.grid(row=1, column=0)

    def create_buttons(self):
        """Creates all the buttons for the calculator."""
        main_frame = Frame(self.root, bg="black", width=360, height=325, padx=0, pady=0, borderwidth=0, highlightthickness=0)
        main_frame.grid(row=1, column=0)

        # Create button frames
        first_frame = Frame(main_frame, bg="black", width=360, height=65, padx=0, pady=0)
        first_frame.grid(row=0, column=0)
        second_frame = Frame(main_frame, bg="black", width=360, height=65, padx=0, pady=0)
        second_frame.grid(row=1, column=0)
        third_frame = Frame(main_frame, bg="black", width=360, height=65, padx=0, pady=0)
        third_frame.grid(row=2, column=0)
        fourth_frame = Frame(main_frame, bg="black", width=360, height=65, padx=0, pady=0)
        fourth_frame.grid(row=3, column=0)
        fifth_frame = Frame(main_frame, bg="black", width=360, height=65, padx=0, pady=0)
        fifth_frame.grid(row=4, column=0)

        # Add images to frames
        self.add_image(first_frame, "assets/exit.png", "assets/exit_clicked.png", 0, lambda e: self.root.destroy())
        self.add_image(first_frame, "assets/00.png", "assets/00_clicked.png", 1, lambda e: self.set_value("00"))
        self.add_image(first_frame, "assets/del.png", "assets/del_clicked.png", 2, lambda e: self.set_value("DEL"))
        self.add_image(first_frame, "assets/ac.png", "assets/ac_clicked.png", 3, lambda e: self.set_value("AC"))

        self.add_image(second_frame, "assets/7.png", "assets/7_clicked.png", 0, lambda e: self.set_value("7"))
        self.add_image(second_frame, "assets/8.png", "assets/8_clicked.png", 1, lambda e: self.set_value("8"))
        self.add_image(second_frame, "assets/9.png", "assets/9_clicked.png", 2, lambda e: self.set_value("9"))
        self.add_image(second_frame, "assets/multiple.png", "assets/multiple_clicked.png", 3, lambda e: self.set_value("*"))

        self.add_image(third_frame, "assets/4.png", "assets/4_clicked.png", 0, lambda e: self.set_value("4"))
        self.add_image(third_frame, "assets/5.png", "assets/5_clicked.png", 1, lambda e: self.set_value("5"))
        self.add_image(third_frame, "assets/6.png", "assets/6_clicked.png", 2, lambda e: self.set_value("6"))
        self.add_image(third_frame, "assets/divide.png", "assets/divide_clicked.png", 3, lambda e: self.set_value("/"))

        self.add_image(fourth_frame, "assets/1.png", "assets/1_clicked.png", 0, lambda e: self.set_value("1"))
        self.add_image(fourth_frame, "assets/2.png", "assets/2_clicked.png", 1, lambda e: self.set_value("2"))
        self.add_image(fourth_frame, "assets/3.png", "assets/3_clicked.png", 2, lambda e: self.set_value("3"))
        self.add_image(fourth_frame, "assets/minus.png", "assets/minus_clicked.png", 3, lambda e: self.set_value("-"))

        self.add_image(fifth_frame, "assets/0.png", "assets/0_clicked.png", 0, lambda e: self.set_value("0"))
        self.add_image(fifth_frame, "assets/dot.png", "assets/dot_clicked.png", 1, lambda e: self.set_value("."))
        self.add_image(fifth_frame, "assets/equal.png", "assets/equal_clicked.png", 2, lambda e: self.set_value("="))
        self.add_image(fifth_frame, "assets/add.png", "assets/add_clicked.png", 3, lambda e: self.set_value("+"))

    def add_image(self, frame, normal_path, clicked_path, col=0, command=None):
        """Adds an image button to the given frame."""
        normal_image = Image.open(normal_path).resize((90, 65))
        clicked_image = Image.open(clicked_path).resize((90, 65))

        tk_normal_image = ImageTk.PhotoImage(normal_image)
        tk_clicked_image = ImageTk.PhotoImage(clicked_image)

        image_label = Label(frame, image=tk_normal_image, padx=0, pady=0, borderwidth=0, highlightthickness=0)
        image_label.image = tk_normal_image

        image_label.grid(row=0, column=col, sticky=N+S+E+W)

        def on_click(event):
            image_label.config(image=tk_clicked_image)
            if command:
                command(event)

        def on_release(event):
            image_label.config(image=tk_normal_image)

        image_label.bind("<Button-1>", on_click)
        image_label.bind("<ButtonRelease-1>", on_release)

        return image_label

    def set_value(self, value):
        """Handles the logic of the calculator."""
        current_value = self.display_label.cget("text")

        if value == "DEL":
            self.display_label.config(text=current_value[:-1])
        elif value == "AC":
            self.display_label.config(text="")
            self.display_label_down.config(text="")
        elif value == "00":
            self.display_label.config(text=current_value + "00")
        elif value == "=":
            try:
                result = str(eval(current_value))
                if result.find("."):
                    result = str(round(float(result), 8))
                self.display_label.config(text=current_value)
                self.display_label_down.config(text="Ans = " + result)
            except NameError:
                self.display_label.config(text="")
                self.display_label_down.config(text="Name Error")
            except ValueError:
                self.display_label.config(text="")
                self.display_label_down.config(text="Value Error")
            except ZeroDivisionError:
                self.display_label.config(text="")
                self.display_label_down.config(text="Zero Division Error")
            except SyntaxError:
                self.display_label.config(text="")
                self.display_label_down.config(text="Syntax Error")
            except Exception as e:
                self.display_label.config(text="")
                self.display_label_down.config(text=f"Invalid Input: {e}")
        else:
            self.display_label.config(text=current_value + value)


if __name__ == "__main__":
    root = Tk()
    app = CalculatorApp(root)
    root.mainloop()
