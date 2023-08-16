import random
import tkinter as tk
from tkinter import messagebox
import subprocess
import os
import sys
import platform

# GimmeKey95 - GUI
# v0.1.0
# Coded by Judith Greaney 2023 (with the assistance of OpenAI's ChatGPT)

# Disallowed product key prefixes
exclusionlist = {"222", "333", "444", "555", "666", "777", "888", "999"}

oemyr = {"95", "96", "97", "98", "99", "00", "01", "02"}

settings = {
    "keytype": "undefd"
}

def retsufgen():
    while True:
        suffix = random.randint(1111111, 9999999)
        if sum(int(digit) for digit in str(suffix)) == 7:
            return suffix

def oemsufgen():
    while True:
        suffix = random.randint(11111, 99999)
        if sum(int(digit) for digit in str(suffix)) == 7:
            return suffix

def keygen(ktype):
    if ktype == "retail":
        prefix = random.randint(111, 999)
        while str(prefix) in exclusionlist:
            prefix = random.randint(111, 999)
        suffix = retsufgen()
        return prefix, suffix
    elif ktype == "OEM":
        day = random.randint(111, 366)
        yr = random.choice(list(oemyr))
        oem = "OEM"
        suffix = oemsufgen()
        oemsuffix = random.randint(11111, 99999)
        return day, yr, oem, suffix, oemsuffix

def keycompile():
    if settings['keytype'] == "retail":
        prefix, suffix = keygen("retail")
        return f"{prefix}-{suffix}"
    elif settings['keytype'] == "OEM":
        day, yr, oem, suffix, oemsuffix = keygen("OEM")
        return f"{day}{yr}-{oem}-00{suffix}-{oemsuffix}"
    else:
        return None

def generate_key():
    key_type = option_var.get()

    if key_type == "Retail":
        # Generate retail key
        settings["keytype"] = "retail"
        key = keycompile()
    elif key_type == "OEM":
        # Generate OEM key
        settings["keytype"] = "OEM"
        key = keycompile()
    else:
        messagebox.showerror("Error", "Please select a key type.")
        return

    if key is not None:
        output_text.delete("1.0", tk.END)  # Clear previous output
        output_text.insert(tk.END, key)

def show_about_dialog():
    messagebox.showinfo("About", "Coded by Judith Greaney 2023\n\nWindows 95 is the intellectual property of Microsoft. I do not own any rights.\n\nVersion 0.1.0")

if __name__ == "__main__":
    # Create the tkinter window
    window = tk.Tk()
    window.title("GimmeKey95 v0.1.0")
    window.geometry("225x163")

    # Option dropdown
    option_var = tk.StringVar()
    option_label = tk.Label(window, text="Select Key Type:")
    option_label.pack()

    option_dropdown = tk.OptionMenu(window, option_var, "Retail", "OEM")
    option_dropdown.pack()

    # Button frame
    button_frame = tk.Frame(window)
    button_frame.pack(pady=10)

    # Generate button
    generate_button = tk.Button(button_frame, text="Generate", command=generate_key, width=10)
    generate_button.pack(side=tk.LEFT, padx=10)

    # About button
    about_button = tk.Button(button_frame, text="About", command=show_about_dialog, width=10)
    about_button.pack(side=tk.LEFT, padx=10)

    # Output text box
    output_label = tk.Label(window, text="Generated Key:")
    output_label.pack()

    output_text = tk.Text(window, height=1, width=30)
    output_text.pack()

    # Start the tkinter event loop
    window.mainloop()
