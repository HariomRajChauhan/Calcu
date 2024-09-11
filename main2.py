from tkinter import *
from PIL import ImageTk, Image


class BaseApp:
    """Base class for common application functionalities."""

    def __init__(self, title="App", geometry="360x390", icon_path=None):
        self.root = Tk()
        self.root.title(title)
        self.root.geometry(geometry)
        if icon_path:
            self.root.iconbitmap(icon_path)
        self.root.resizable(False, False)
        
    def create_frame(self, parent, bg="black", width=360, height=65, row=0, column=0):
        """Create a frame with specified parameters."""
        frame = Frame(parent, bg=bg, width=width, height=height)
        frame.grid(row=row, column=column, sticky=N+S+E+W)
        return frame

    def start(self):
        """Start the main event loop."""
        self.root.mainloop()


class CalculatorApp(BaseApp):
    """Calculator application that inherits from BaseApp."""
    
    def __init__(self):
        # Call the BaseApp constructor
        super().__init__(title="Calculator", geometry="360x390", icon_path="assets/icon.ico")
        self.display_label = None
        self.display_label_down = None
        self.create_display()
        self.create_buttons()

    def create_display(self):
        """Create the calculator display."""
        display_frame = self.create_frame(self.root, width=360, height=65)
        
        self.display_label = Label(display_frame, text="", font=("monospace", 30), padx=0, pady=0, fg="black", borderwidth=0, highlightthickness=0)
        self.display_label.grid(row=0, column=0, sticky=W)

        self.display_label_down = Label(display_frame, text="", font=("monospace", 22), padx=0, pady=0, fg="black", borderwidth=0, highlightthickness=0)
        self.display_label_down.grid(row=1, column=0, sticky=W)

    def create_buttons(self):
        """Create the calculator buttons."""
        main_frame = self.create_frame(self.root, width=360, height=325, row=1)
        
        # Add frames for button rows
        button_frames = [self.create_frame(main_frame, row=i) for i in range(5)]

        # Add images to frames using method overloading (polymorphism)
        self.add_image(button_frames[0], "assets/exit.png", "assets/exit_clicked.png", 0, self.on_exit)
        self.add_image(button_frames[0], "assets/00.png", "assets/00_clicked.png", 1, lambda e: self.set_value("00"))
        self.add_image(button_frames[0], "assets/del.png", "assets/del_clicked.png", 2, lambda e: self.set_value("DEL"))
        self.add_image(button_frames[0], "assets/ac.png", "assets/ac_clicked.png", 3, lambda e: self.set_value("AC"))

        # Row 2
        self.add_image(button_frames[1], "assets/7.png", "assets/7_clicked.png", 0, lambda e: self.set_value("7"))
        self.add_image(button_frames[1], "assets/8.png", "assets/8_clicked.png", 1, lambda e: self.set_value("8"))
        self.add_image(button_frames[1], "assets/9.png", "assets/9_clicked.png", 2, lambda e: self.set_value("9"))
        self.add_image(button_frames[1], "assets/multiple.png", "assets/multiple_clicked.png", 3, lambda e: self.set_value("*"))

        # Row 3
        self.add_image(button_frames[2], "assets/4.png", "assets/4_clicked.png", 0, lambda e: self.set_value("4"))
        self.add_image(button_frames[2], "assets/5.png", "assets/5_clicked.png", 1, lambda e: self.set_value("5"))
        self.add_image(button_frames[2], "assets/6.png", "assets/6_clicked.png", 2, lambda e: self.set_value("6"))
        self.add_image(button_frames[2], "assets/divide.png", "assets/divide_clicked.png", 3, lambda e: self.set_value("/"))

        # Row 4
        self.add_image(button_frames[3], "assets/1.png", "assets/1_clicked.png", 0, lambda e: self.set_value("1"))
        self.add_image(button_frames[3], "assets/2.png", "assets/2_clicked.png", 1, lambda e: self.set_value("2"))
        self.add_image(button_frames[3], "assets/3.png", "assets/3_clicked.png", 2, lambda e: self.set_value("3"))
        self.add_image(button_frames[3], "assets/minus.png", "assets/minus_clicked.png", 3, lambda e: self.set_value("-"))

        # Row 5
        self.add_image(button_frames[4], "assets/0.png", "assets/0_clicked.png", 0, lambda e: self.set_value("0"))
        self.add_image(button_frames[4], "assets/dot.png", "assets/dot_clicked.png", 1, lambda e: self.set_value("."))
        self.add_image(button_frames[4], "assets/equal.png", "assets/equal_clicked.png", 2, lambda e: self.set_value("="))
        self.add_image(button_frames[4], "assets/add.png", "assets/add_clicked.png", 3, lambda e: self.set_value("+"))

    def add_image(self, frame, normal_path, clicked_path, col=0, command=None):
        """Add an image button to the frame, overloaded for default command."""
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
        """Handle calculator operations."""
        current_value = self.display_label.cget("text")

        if value == "DEL":
            self.display_label.config(text=current_value[:-1])
        elif value == "AC":
            self.display_label.config(text="")
            self.display_label_down.config(text="")
        elif value == "00":
            self.display_label.config(text=current_value + "00")
        elif value == "=":
            self.calculate_result(current_value)
        else:
            self.display_label.config(text=current_value + value)

    def calculate_result(self, expression):
        """Calculate and display the result."""
        try:
            result = str(eval(expression))
            if result.find("."):
                result = str(round(float(result), 8))
            self.display_label.config(text=expression)
            self.display_label_down.config(text="Ans = " + result)
        except (NameError, ValueError, ZeroDivisionError, SyntaxError) as e:
            self.display_label.config(text="")
            self.display_label_down.config(text=f"{type(e).__name__}")
        except Exception as e:
            self.display_label.config(text="")
            self.display_label_down.config(text=f"Invalid Input: {e}")

    def on_exit(self, event):
        """Handle the exit command."""
        self.root.destroy()


if __name__ == "__main__":
    app = CalculatorApp()
    app.start()