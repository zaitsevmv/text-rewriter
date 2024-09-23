import tkinter as tk

class App():
    def __init__(self, f1, f2) -> None:
        self.func1 = f1
        self.func2 = f2
        self.current_func = self.func1

        self.root = tk.Tk()
        self.root.title("Rephrase Text")
        self.root.geometry("1000x550")

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
                result_textbox.config(state=tk.NORMAL)  
                result_textbox.delete("1.0", tk.END)   
                result_textbox.insert(tk.END, new_text) 
                result_textbox.config(state=tk.DISABLED)

        entry_frame = tk.Frame(self.root)
        entry_frame.pack(pady=10)

        entry_label = tk.Label(entry_frame, text="Enter text to rephrase:", font=('Arial', 12))
        entry_label.pack(anchor="w", padx=10)

        entry = tk.Text(entry_frame, height=8, width=100, font=('Arial', 10))
        entry.pack(padx=10, pady=5)

        button = tk.Button(self.root, text="Rephrase", command=on_button_click, bg="#4CAF50", fg="white", font=('Arial', 12))
        button.pack(pady=10)

        switch_button = tk.Button(self.root, text="Switch API", command=on_switch_click, bg="#f0ad4e", fg="white", font=('Arial', 12))
        switch_button.pack(pady=5)

        api_label = tk.Label(self.root, text="Random API", font=('Arial', 12), fg="blue")
        api_label.pack(pady=5)

        result_frame = tk.Frame(self.root)
        result_frame.pack(pady=10, fill="both", expand=True)

        scrollbar = tk.Scrollbar(result_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        result_textbox = tk.Text(result_frame, height=10, width=100, font=('Arial', 12), wrap=tk.WORD, yscrollcommand=scrollbar.set)
        result_textbox.pack(pady=5, padx=10)
        result_textbox.config(state=tk.DISABLED) 

        scrollbar.config(command=result_textbox.yview)

    def Start(self):
        self.root.mainloop()

