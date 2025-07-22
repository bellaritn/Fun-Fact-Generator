import tkinter as tk
from tkinter import messagebox , scrolledtext
import random 
import os

def get_fact():
    try:
        with open("FunFacts.txt", "r") as file:
            available_facts= [f.strip() for f in file.readlines() if f.strip()]
        with open("UsedFacts.txt", "r") as file:
            used_facts = [f.strip() for f in file.readlines() if f.strip()]
        if not available_facts:
            messagebox.showerror("Error", "No more facts available. Resetting  used facts.:")
            reset()
            return
        unused_facts = [f for f in available_facts if f not in used_facts]
        if not unused_facts:
            messagebox.showinfo("Info", "All facts have been used. Resetting used facts.")
            reset()
            return
        fact = random.choice(unused_facts)
        messagebox.showinfo("Fun Fact", fact)

        with open("UsedFacts.txt", "a") as file:
            file.write(fact + "\n")
    except FileNotFoundError:
        messagebox.showerror("Error", "FunFacts.txt file not found. Please create it with some facts.")

def reset():
    try:
        with open("FunFacts.txt", "r") as fun_file:
            fun_facts = [f.strip() for f in fun_file.readlines() if f.strip()]
        
        with open("UsedFacts.txt", "r") as used_file:
            used_facts = [f.strip() for f in used_file.readlines() if f.strip()]
            
        all_facts = list(set(fun_facts + used_facts))  # Remove duplicates
        
        with open("FunFacts.txt", "w") as file:
            for fact in all_facts:

                file.write(fact + "\n")
        open("UsedFacts.txt", "w").close()
    
        messagebox.showinfo("Info", "Reset used facts successfully!")

    except FileNotFoundError:
        messagebox.showerror("Error", "UsedFacts.txt file not found. Please create it first.")
        
def show_used_facts():
    try:
        with open("UsedFacts.txt", "r") as file:
             used_facts = [f.strip() for f in file.readlines() if f.strip()]
         
        if not used_facts:
            messagebox.showinfo("Used Facts", "No facts have been used yet.")   
            return

        used_window= tk.Toplevel()
        used_window.title("Used Facts")

        text_area = scrolledtext.ScrolledText(used_window, width=50, height=20 , wrap=tk.WORD)
        text_area.pack(padx=10, pady=10)

        for fact in used_facts:
            text_area.insert(tk.END, fact.strip() + "\n" + "\n")
        text_area.config(state=tk.DISABLED)  

    except FileNotFoundError:
        messagebox.showerror("Error", "UsedFacts.txt file not found. Please create it first.")



if __name__ == "__main__":
    root = tk.Tk()
    root.title("Fun Fact Generator")
    root.geometry("300x200")
    
    label = tk.Label(root, text="Click the button to get a fun fact!")
    label.pack(pady=10)
    
    button = tk.Button(root, text="Get Fun Fact", command=get_fact)
    button.pack(pady=10)

    reset_button = tk.Button(root, text="Reset Used Facts", command=reset)
    reset_button.pack(pady=5)

    used_facts= tk.Button(root, text="show used facts",command=show_used_facts)
    used_facts.pack(pady=5)

    root.mainloop()
