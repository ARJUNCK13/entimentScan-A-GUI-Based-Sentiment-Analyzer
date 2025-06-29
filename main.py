import tkinter as tk
from tkinter import messagebox
from sentiment_model import load_model

# Load sentiment model
model = load_model()

# Initial theme state
current_theme = "dark"

# Analyze sentiment
def analyze_sentiment():
    text = entry.get()
    if not text.strip():
        messagebox.showwarning("Input Error", "Please enter a sentence.")
        return

    result = model.predict([text])[0]
    if result == "positive":
        emoji = "😊"
        color = "green"
    else:
        emoji = "😡"
        color = "red"

    result_label.config(text=f"{emoji} Sentiment: {result.capitalize()}", fg=color)

# Clear text and result
def clear_text():
    entry.delete(0, tk.END)
    result_label.config(text="")

# Toggle between dark and light theme
def toggle_theme():
    global current_theme
    if current_theme == "dark":
        root.configure(bg="white")
        title.config(bg="white", fg="black")
        result_label.config(bg="white", fg="black")
        theme_btn.config(text="🌙 Dark Mode", bg="#e0e0e0", fg="black")
        current_theme = "light"
    else:
        root.configure(bg="#1e1e1e")
        title.config(bg="#1e1e1e", fg="white")
        result_label.config(bg="#1e1e1e", fg="white")
        theme_btn.config(text="☀️ Light Mode", bg="#2d2d2d", fg="white")
        current_theme = "dark"

# Create main window
root = tk.Tk()
root.title("Sentiment Analyzer")
root.geometry("450x300")
root.configure(bg="#1e1e1e")  # Default dark mode

# Title
title = tk.Label(root, text="Sentiment Analyzer", font=("Arial", 18, "bold"), bg="#1e1e1e", fg="white")
title.pack(pady=15)

# Text entry
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=10)

# Analyze button
analyze_btn = tk.Button(root, text="🔍 Analyze", font=("Arial", 12), bg="#2d2d2d", fg="white", command=analyze_sentiment)
analyze_btn.pack(pady=5)

# Clear button
clear_btn = tk.Button(root, text="❌ Clear", font=("Arial", 12), bg="#2d2d2d", fg="white", command=clear_text)
clear_btn.pack(pady=5)

# Theme toggle button
theme_btn = tk.Button(root, text="☀️ Light Mode", font=("Arial", 12), bg="#2d2d2d", fg="white", command=toggle_theme)
theme_btn.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14), bg="#1e1e1e")
result_label.pack(pady=15)

# Start GUI
root.mainloop()
