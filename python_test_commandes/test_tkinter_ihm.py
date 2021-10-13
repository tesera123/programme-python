from sys import version_info
import tkinter as tk

app = tk.Tk()
button1 = tk.Button(app, text="Python Label 1")
button2 = tk.Button(app, text="Python Label 2")
button1.pack(side=tk.LEFT)
button2.pack(side=tk.LEFT)
app.mainloop()