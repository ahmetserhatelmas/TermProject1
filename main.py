import tkinter as tk
from tkinter import ttk
import time
import openai

openai.api_key = "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"


# Create a function to handle the user input and display the answer
def get_answer():
    city = entry.get()
    question = f"Can you give me some general information about the city of {city} in about 100-150 words and write quickly please."
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}]
    )
    reply = response["choices"][0]["message"]["content"]

    # Split the answer into words
    words = reply.split()

    # Clear the text widget
    answer_text.config(state="normal")
    answer_text.delete("1.0", tk.END)

    # Display the answer word by word
    for word in words:
        answer_text.insert(tk.END, word + " ")
        answer_text.see("end")
        answer_text.update()
        time.sleep(0.1)  # Delay between each word display

    # Disable editing of the text widget
    answer_text.config(state="disabled")


# Create a function to clear the fields
def clear_fields():
    entry.delete(0, tk.END)  # Clear the Entry widget
    answer_text.config(state="normal")
    answer_text.delete("1.0", tk.END)  # Clear the text widget
    answer_text.config(state="disabled")  # Disable editing of the text widget


# Create a function to exit the application
def exit_app():
    root.destroy()  # Close the window and exit the application


# Create the main window
root = tk.Tk()
root.title("Wikipedia of cities")
root.config(padx=50, pady=50, bg="#B1DDC6")

# Create the user interface elements using grid geometry manager
label = tk.Label(root, text="Enter name of a city:", font=("Arial", 10, "bold"), background="#B1DDC6")
label.grid(row=0, column=0)

entry = tk.Entry(root, width=30)
entry.grid(row=0, column=1, columnspan=1)

button1 = tk.Button(root, text="Confirm", highlightthickness=0, width=15, command=get_answer)
button1.grid(row=1, column=1, pady=5)

# Create a scrollable text widget to display the answer
scrollbar = ttk.Scrollbar(root)
scrollbar.grid(row=2, column=2, sticky="NS")

answer_text = tk.Text(root, wrap="word", yscrollcommand=scrollbar.set, height=10, width=50)
answer_text.config(state="disabled")  # Disable editing of the text widget
answer_text.grid(row=2, column=0, columnspan=2, rowspan=2, padx=5, pady=5, sticky="NESW")

scrollbar.config(command=answer_text.yview)

button2 = tk.Button(root, text="Clear", highlightthickness=0, width=15, command=clear_fields)
button2.grid(row=4, column=0, pady=5)

button3 = tk.Button(root, text="Exit", highlightthickness=0, width=15, command=exit_app)
button3.grid(row=4, column=1, pady=5)

# Set grid weights to allow the widgets to expand and fill the available space
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(2, weight=1)


root.mainloop()
