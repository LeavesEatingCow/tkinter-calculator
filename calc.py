import tkinter as tk


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

    # Run the app
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()