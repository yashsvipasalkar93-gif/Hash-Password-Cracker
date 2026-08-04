# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 22:17:51 2026

@author: YASHASWI
"""

import hashlib
import tkinter as tk
from tkinter import messagebox
import time
from PIL import Image, ImageTk

# Function to update clock
def update_clock():
    current_time = time.strftime("%H:%M:%S")
    clock_label.config(text="Time: " + current_time)
    window.after(1000, update_clock)

def crack_password():
    target_hash = entry.get().strip()

    if not target_hash:
        messagebox.showwarning("Input Error", "Please enter a hash")
        return

    start_time = time.time()  # start timer

    try:
        with open("wordlist.txt", "r") as file:
            for word in file:
                word = word.strip()
                hashed = hashlib.sha256(word.encode()).hexdigest()

                if hashed == target_hash:
                    end_time = time.time()
                    time_taken = round(end_time - start_time, 2)

                    messagebox.showinfo(
                        "Result",
                        f"Password Found: {word}\nTime Taken: {time_taken} seconds"
                    )
                    return

        end_time = time.time()
        time_taken = round(end_time - start_time, 2)

        messagebox.showinfo(
            "Result",
            f"Password not found\nTime Taken: {time_taken} seconds"
        )

    except FileNotFoundError:
        messagebox.showerror("Error", "wordlist.txt not found")

# GUI Window
window = tk.Tk()
window.title("Password Cracker Tool")
window.geometry("920x620")
window.config(bg="#0f172a")

# Load background image
img = Image.open("bg.jpeg")   # your jpeg file name
img = img.resize((920, 620))

bg_image = ImageTk.PhotoImage(img)

bg_label = tk.Label(window, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# VERY IMPORTANT (fix error)
bg_label.image = bg_image

# Create a Frame 
frame = tk.Frame(window, bg="#0f172a")
frame.place(relx=0.5, rely=0.5, anchor="center")

frame.lift()


terminal = tk.Label(window, text="Initializing attack...",
                    fg="#22c55e", bg="#0f172a",
                    font=("Verdana", 14))
terminal.place(x=10, y=580)

#Use the frame

# Title
title = tk.Label(frame, text="Dictionary Attack Tool",
                 fg="red", bg="#0f172a", font=("Verdana",24,"bold"))
title.pack(pady=15)

# Clock
clock_label = tk.Label(frame, fg="#38bdf8", bg="#0f172a", font=("Arial", 12))
clock_label.pack()
update_clock()

# Instruction
label = tk.Label(frame, text="Enter SHA-256 Hash",
                 fg="white", bg="#0f172a", font=("Segoe UI", 14,"bold"))
label.pack(pady=15)

# Entry
entry = tk.Entry(frame, width=50)
entry.pack()

# Button
button = tk.Button(frame, text="Start Dictionary Attack",
                   bg="#2563eb", fg="yellow", font=("Lucida Console", 11, "bold"),
                   command=crack_password)
button.pack(pady=25)

# Footer
footer = tk.Label(frame, text="HASHED PASSWORD CRACKER",
                  fg="orange", bg="#0f172a", font=("Tahoma", 9))
footer.pack(side="bottom", pady=10)

# typing Effect 
def typing_effect(text, label):
    for i in range(len(text)+1):
        label.config(text=text[:i])
        window.update()
        time.sleep(0.03)
        typing_effect("Dictionary Attack Tool", title)


window.mainloop()