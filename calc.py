import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
DIGITS_FONT_STYLE = ("Arial", 24, "bold")
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = "#F8FAFF"
WHITE = "#FFFFFF"
LIGHT_BLUE = "#CCEDFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"


class Calculator:

    def __init__(self):
        """
            1. Create Window for application
            2. Define dimensions of the app (standard iPhone 8 dimensions)
            3. Disabled resizing window
            4. Gave app the title of Calculator
        """
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total_expression = "0"
        self.current_expression = "0"

        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}

        self.button_frame = self.create_buttons_frame()

        # This fills up buttons to fit entire frame
        self.button_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.button_frame.rowconfigure(x, weight=1)
            self.button_frame.columnconfigure(x, weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_specials_buttons()

    def create_specials_buttons(self):
        self.create_clear_button()
        self.create_equals_button()

    def create_display_labels(self):
        # Creates a total label and puts it on the display frame
        # Label equates to the value of the total expression
        # Anchor Labels to the East side of the frame
        # Set background color to Light Gray and foreground color to custom color
        # Set up different font from default to be small
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill="both")

        # Label equates to the value of the current expression
        # Set up different font from default to be large
        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                         fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)

        label.pack(expand=True, fill="both")

        return total_label, label

    def create_display_frame(self):
        # Set a frame on the main window with height 221 with LIGHT_GRAY background
        frame = tk.Frame(self.window, heigh=221, bg=LIGHT_GRAY)

        # Frame will expand and fill any empty space around it
        frame.pack(expand=True, fill="both")

        return frame

    def create_digit_buttons(self):
        # Place buttons in button frame
        # Text is the digit
        # Value of self.digits is the row, column placement
        # Buttons fill up every side and fills up grid with sticky argument NSEW
        # Removed borders
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.button_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,
                               borderwidth=0)
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.button_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0)
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def create_clear_button(self):
        # Column span determines how many spaces in a row the button can take in a row
        button = tk.Button(self.button_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=0, column=1, columnspan=3, sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(self.button_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    # Run the app
    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
