import tkinter as tk

class App():
    root = tk.Tk()

    def __init__(self) -> None:
        self.root.title("Text to emoji")

        self.root.geometry("400x300")

        label = tk.Label(self.root, text="Hello, welcome to your desktop app!", font=('Arial', 14))
        label.pack(pady=20)

        def on_button_click():
            label.config(text="Button Clicked!")

        button = tk.Button(self.root, text="Click Me", command=on_button_click)
        button.pack(pady=10)

    def Start(self):
        self.root.mainloop()
