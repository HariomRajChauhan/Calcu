# CALCU - A GUI Application

This is a simple calculator application built using Python's Tkinter library. The calculator provides a graphical user interface (GUI) for performing basic arithmetic operations. The interface uses images for buttons, enhancing the visual appearance and user experience.

## Features

- **Basic Arithmetic Operations**: Supports addition, subtraction, multiplication, and division.
- **Clear Functionality**: "AC" button to clear all input and "DEL" button to delete the last character.
- **Error Handling**: Displays specific error messages for invalid inputs, such as syntax errors, division by zero, and more.
- **Double Zero Button**: Includes a "00" button to quickly add two zeros to the input.
- **Interactive GUI**: Uses image buttons for a visually appealing interface.
- **Upcomming New Features**: Curently I am writing its new features for its advance version ie:-(Scientific Calculator)

## Prerequisites

Make sure you have the following installed on your system:

- Python 3.x
- Tkinter (usually included with Python)
- Pillow (Python Imaging Library) for handling images

To install Pillow, run:

```bash
pip install pillow
```

## Getting Started

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/HariomRajChauhan/Calcu.git
   cd Calcu
   ```

2. **Add Assets**:

   Make sure you have all the required image assets in the `assets` directory:
   - `exit.png`
   - `00.png`
   - `del.png`
   - `ac.png`
   - `1.png` to `9.png`
   - `0.png`, `dot.png`, `equal.png`, `add.png`, `minus.png`, `divide.png`, `multiple.png`
   - `icon.ico` for the application icon

3. **Run the Application**:

   Execute the script using Python:

   ```bash
   python main.py
   ```

   The calculator GUI will open and be ready for use.

4. **Convet .py to .exe**:
   Install pyinstaller using pip:

   ```bash
   pip install pyinstaller
   ```

   Install pywin32 using pip:

   ```bash
   pip install pywin32
   ```

   Dependencies: `pythoncom`, `pywintypes`

   Convert the script to an executable:

   ```bash
   pyinstaller --onefile --windowed main.py
   pyinstaller --onefile main.py
   ```

   OR

   ```bash
   python -m PyInstaller ./main.py --onefile
   ```

   The `main.spec` file should be like this:

   ```bash
   ![main_spec_file](main.spec)
   ```

   After adding the path of the icon file in the `main.spec` file, run the following command in CMD in that curent directory:

   ```bash
   python -m PyInstaller ./main.spec
   ```

   Executable Program:
   The calculator GUI EXE will be maked in your `./dist` directory.

   ```bash
   ./dist/main.exe
   ```

## Usage

- **Number Buttons**: Click the number buttons (0-9) to enter digits.
- **Operators**: Click on `+`, `-`, `*`, `/` for the respective arithmetic operations.
- **Equals (`=`)**: Calculates the result of the entered expression.
- **Delete (`DEL`)**: Deletes the last entered character.
- **Clear (`AC`)**: Clears the current input.
- **Double Zero (`00`)**: Adds two zeros to the current input.

## File Structure

```plaintext
Calcu
│
├── main.py              # Main application script
├── README.md            # This readme file
└── assets/              # Directory containing all image assets
    ├── icon.ico
    ├── exit.png
    ├── 00.png
    ├── del.png
    ├── ac.png
    ├── 1.png to 9.png
    ├── dot.png
```

## Error Handling

- **Name Error**: Displayed when an invalid name is used in the expression.
- **Value Error**: Displayed when an invalid value is used.
- **Zero Division Error**: Displayed when division by zero is attempted.
- **Syntax Error**: Displayed when there is an invalid syntax in the expression.
- **Invalid Input**: General error message for any other exceptions.

## GUI Screenshot

![GUI_screenshot](assets/CAlculator.png)

## License

This project is under Hariom Raj Chauhan.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or report an issue.

## Acknowledgments

- Thanks to the Python and Tkinter communities for their excellent resources and support.
