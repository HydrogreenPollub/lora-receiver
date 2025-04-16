import tkinter as tk

def read_lora():
    print("Reading from LORA")

root = tk.Tk()
root.title("LORA reader")
root.resizable(False, False)

banner = tk.Label(root, text="LORA Receiver")
banner.pack()

start_button = tk.Button(root, text="Start Reading", command=read_lora)


root.mainloop()
