import secrets
import tkinter as tk
import os
import sys

def link(lists):
    return [item for sublist in lists for item in sublist]

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

class Texts:
    def __init__(self):
        self.a_z = [chr(i) for i in range(97, 123)]
        self.A_Z = [chr(i) for i in range(65, 91)]
        self.number = [chr(i) for i in range(48, 58)]
        self.sign = ["!", "#", "$", "%", "&", "-", "^", "[", ":", "]", "=", "~", "{", "+", "*", "}", "<", ">", "?", "@"]
        self.all = link([self.a_z, self.A_Z, self.number, self.sign])

    def gen(self, chars, length):
        return "".join(secrets.choice(chars) for _ in range(length))

def output():
    try:
        length = int(entry.get())
        if length <= 0:
            raise ValueError("Length must be positive.")
    except ValueError:
        length = secrets.choice(range(14, 17))

    if mode_bar[0].get():
        chrs_bar[0].set(True)
        chrs_bar[1].set(False)
        chrs_bar[2].set(True)
        chrs_bar[3].set(False)
        length = secrets.choice(range(14, 17))

    if mode_bar[1].get():
        chrs_bar[0].set(True)
        chrs_bar[1].set(True)
        chrs_bar[2].set(True)
        chrs_bar[3].set(True)
        length = secrets.choice(range(14, 17))

    chars = []
    if chrs_bar[0].get():
        chars += texts.a_z
    if chrs_bar[1].get():
        chars += texts.A_Z
    if chrs_bar[2].get():
        chars += texts.number
    if chrs_bar[3].get():
        chars += texts.sign

    chars = chars or texts.all
    output_text.delete("1.0", tk.END)
    output_text.insert("1.0", texts.gen(chars, length))

    mode_bar[0].set(False)
    mode_bar[1].set(False)

if __name__ == "__main__":
    root = tk.Tk()
    root.iconbitmap(resource_path("icon.ico"))
    root.title("Random String")
    root.geometry("260x180")
    root.resizable(False, False)

    bg_color = "#0f0f0f"
    fg_color = "#A9DFBF"
    root.configure(bg=bg_color)

    texts = Texts()
    FONT = ("Consolas", 10)

    MODE = ["Email", "Password"]
    mode_bar = [tk.BooleanVar(value=False) for _ in MODE]
    for i, mode in enumerate(MODE):
        check = tk.Checkbutton(root, text=mode, font=FONT, variable=mode_bar[i], fg=fg_color, bg=bg_color, selectcolor=bg_color, activeforeground=fg_color)
        check.place(x=i * 80, y=0)

    ITEM = ["a-z", "A-Z", "0-9", "Symbols"]
    chrs_bar = [tk.BooleanVar(value=False) for _ in ITEM]
    for i, item in enumerate(ITEM):
        check = tk.Checkbutton(root, text=item, font=FONT, variable=chrs_bar[i], fg=fg_color, bg=bg_color, selectcolor=bg_color, activeforeground=fg_color)
        check.place(x=i * 60, y=25)

    entry = tk.Entry(root, width=35, bg=bg_color, fg=fg_color, insertbackground=fg_color)
    entry.place(x=5, y=50)

    button = tk.Button(root, text="Generate", font=FONT, command=output, fg=fg_color, bg=bg_color, activeforeground=fg_color, activebackground="#4D4D4D")
    button.place(x=5, y=75)

    output_text = tk.Text(root, width=30, height=3, font=FONT, bg=bg_color, fg=fg_color, insertbackground=fg_color)
    output_text.place(x=5, y=115)

    root.mainloop()
