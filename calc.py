import tkinter as tk

LIGHT_GRAY = "#F5F5F5"
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
        self.window.resizable(0,0)
        self.window.title("Calculator")

        self.display_fram = self.create_display_frame()
        self.button_frame = self.create_buttons_frame()

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