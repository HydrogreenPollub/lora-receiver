import serial
import tkinter as tk

from flatbuffers import TSData

def read_lora():
    print("Reading from LORA")

    # TODO find right device
    with serial.Serial("/dev/ttyS0", 125200, timeout=1) as s:
        if s.in_waiting > 0:
            raw_data = s.read(s.in_waiting)
            data = TSData.TSData.GetRootAs(raw_data, 0)

root = tk.Tk()
root.title("LORA reader")
root.resizable(False, False)

banner = tk.Label(root, text="LORA Receiver")
banner.pack()

start_button = tk.Button(root, text="Start Reading", command=read_lora)


root.mainloop()
