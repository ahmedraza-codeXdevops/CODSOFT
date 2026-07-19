import tkinter as tk
from tkinter import messagebox

contacts = []

def refresh_list():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)

def add_contact():
    name = name_entry.get().strip()
    phone = phone_entry.get().strip()
    email = email_entry.get().strip()
    address = address_entry.get().strip()

    if name == "" or phone == "":
        messagebox.showerror("Error", "Name and Phone are required.")
        return

    contacts.append({
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address
    })

    refresh_list()
    clear_fields()
    messagebox.showinfo("Success", "Contact Added Successfully!")

def show_contact(event):
    if not listbox.curselection():
        return

    index = listbox.curselection()[0]
    contact = contacts[index]

    clear_fields()

    name_entry.insert(0, contact["Name"])
    phone_entry.insert(0, contact["Phone"])
    email_entry.insert(0, contact["Email"])
    address_entry.insert(0, contact["Address"])

def update_contact():
    if not listbox.curselection():
        messagebox.showerror("Error", "Select a contact first.")
        return

    index = listbox.curselection()[0]

    contacts[index] = {
        "Name": name_entry.get().strip(),
        "Phone": phone_entry.get().strip(),
        "Email": email_entry.get().strip(),
        "Address": address_entry.get().strip()
    }

    refresh_list()
    messagebox.showinfo("Success", "Contact Updated Successfully!")

def delete_contact():
    if not listbox.curselection():
        messagebox.showerror("Error", "Select a contact first.")
        return

    index = listbox.curselection()[0]
    del contacts[index]

    refresh_list()
    clear_fields()

    messagebox.showinfo("Success", "Contact Deleted Successfully!")

def search_contact():
    keyword = search_entry.get().strip().lower()

    listbox.delete(0, tk.END)

    for contact in contacts:
        if keyword in contact["Name"].lower() or keyword in contact["Phone"]:
            listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

root = tk.Tk()
root.title("Contact Book")
root.geometry("700x550")
root.resizable(False, False)

title = tk.Label(root, text="Contact Book", font=("Arial", 20, "bold"))
title.pack(pady=10)

frame = tk.Frame(root)
frame.pack()

tk.Label(frame, text="Name").grid(row=0, column=0, padx=5, pady=5)
name_entry = tk.Entry(frame, width=30)
name_entry.grid(row=0, column=1)

tk.Label(frame, text="Phone").grid(row=1, column=0, padx=5, pady=5)
phone_entry = tk.Entry(frame, width=30)
phone_entry.grid(row=1, column=1)

tk.Label(frame, text="Email").grid(row=2, column=0, padx=5, pady=5)
email_entry = tk.Entry(frame, width=30)
email_entry.grid(row=2, column=1)

tk.Label(frame, text="Address").grid(row=3, column=0, padx=5, pady=5)
address_entry = tk.Entry(frame, width=30)
address_entry.grid(row=3, column=1)

button_frame = tk.Frame(root)
button_frame.pack(pady=15)

tk.Button(button_frame, text="Add Contact", width=15, command=add_contact).grid(row=0, column=0, padx=5)
tk.Button(button_frame, text="Update Contact", width=15, command=update_contact).grid(row=0, column=1, padx=5)
tk.Button(button_frame, text="Delete Contact", width=15, command=delete_contact).grid(row=0, column=2, padx=5)
tk.Button(button_frame, text="Clear", width=15, command=clear_fields).grid(row=0, column=3, padx=5)

search_frame = tk.Frame(root)
search_frame.pack(pady=10)

search_entry = tk.Entry(search_frame, width=35)
search_entry.grid(row=0, column=0, padx=5)

tk.Button(search_frame, text="Search", width=15, command=search_contact).grid(row=0, column=1, padx=5)
tk.Button(search_frame, text="Show All", width=15, command=refresh_list).grid(row=0, column=2, padx=5)

listbox = tk.Listbox(root, width=70, height=15)
listbox.pack(pady=15)

listbox.bind("<<ListboxSelect>>", show_contact)

root.mainloop()
