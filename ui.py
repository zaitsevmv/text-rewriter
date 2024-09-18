import tkinter as tk

class App():
    def __init__(self, f1, f2) -> None:
        self.func1 = f1
        self.func2 = f2
        self.current_func = self.func1

        self.root = tk.Tk()
        self.root.title("Rephrase Text")
        self.root.geometry("500x400")

        def on_switch_click():
            if self.current_func == self.func1:
                self.current_func = self.func2
                api_label.config(text="Gigachat API")
            else:
                self.current_func = self.func1
                api_label.config(text="Random API")

        def on_button_click():
            input_text = entry.get("1.0", tk.END).strip()
            if input_text:
                new_text = self.current_func(input_text)
                label.config(text=new_text)

        # Frame for the text entry
        entry_frame = tk.Frame(self.root)
        entry_frame.pack(pady=10)

        # Entry box for input text
        entry_label = tk.Label(entry_frame, text="Enter text to rephrase:", font=('Arial', 12))
        entry_label.pack(anchor="w", padx=10)

        entry = tk.Text(entry_frame, height=4, width=50, font=('Arial', 10))
        entry.pack(padx=10, pady=5)

        # Button to trigger rephrase
        button = tk.Button(self.root, text="Rephrase", command=on_button_click, bg="#4CAF50", fg="white", font=('Arial', 12))
        button.pack(pady=10)

        # Button to switch between APIs
        switch_button = tk.Button(self.root, text="Switch API", command=on_switch_click, bg="#f0ad4e", fg="white", font=('Arial', 12))
        switch_button.pack(pady=5)

        # Label to show which API is currently in use
        api_label = tk.Label(self.root, text="Random API", font=('Arial', 12), fg="blue")
        api_label.pack(pady=5)

        # Label to show the rephrased text output
        label_frame = tk.Frame(self.root)
        label_frame.pack(pady=10)

        result_label = tk.Label(label_frame, text="Rephrased Text:", font=('Arial', 12))
        result_label.pack(anchor="w", padx=10)

        label = tk.Label(label_frame, text="", font=('Arial', 12), wraplength=400, justify="left", bg="lightgray", height=6, width=50)
        label.pack(pady=5, padx=10)

    def Start(self):
        self.root.mainloop()

