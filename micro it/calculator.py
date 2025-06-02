import tkinter as tk


def on_click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = eval(str(entry_var.get()))
            entry_var.set(result)
        except:
            entry_var.set("Error")
    elif text == "C":
        entry_var.set("")
    else:
        entry_var.set(entry_var.get() + text)


root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Arial 20", bd=10, relief=tk.RIDGE, justify=tk.RIGHT)
entry.pack(fill=tk.BOTH, padx=10, pady=10, ipady=10)


buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]


for row_values in buttons:
    row_frame = tk.Frame(root)
    row_frame.pack(expand=True, fill="both")
    for btn_text in row_values:
        button = tk.Button(row_frame, text=btn_text, font="Arial 18", bd=5)
        button.pack(side="left", expand=True, fill="both")
        button.bind("<Button-1>", on_click)


root.mainloop()
