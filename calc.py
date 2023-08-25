import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
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
        self.button_frame = self.create_buttons_frame()

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
