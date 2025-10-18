# 💞 Match Calculator - Tkinter GUI
from tkinter import *

# Create main window
root = Tk()
root.title("Match Calculator 💞")
root.geometry("420x360")
root.config(bg="#e6f2ff")

# -------------------------------
# Function to calculate match %
# -------------------------------
def calculate_match():
    name_a = name1.get().strip().lower()
    name_b = name2.get().strip().lower()

    if name_a == "" or name_b == "":
        result_label.config(text="⚠️ Please enter both names!", fg="#cc0000")
        return

    # Combine both names and create a repeatable match score
    combined = name_a + name_b
    match_score = sum(ord(c) for c in combined) % 101  # 0–100%

    # Generate message based on compatibility
    if match_score < 40:
        message = "🤝 Not the strongest match, but opposites attract!"
    elif 40 <= match_score < 70:
        message = "😊 You two have decent compatibility!"
    else:
        message = "🌟 Great match! You vibe really well!"

    # Display result
    result_label.config(
        text=f"{name_a.title()} 💫 {name_b.title()}\nMatch Percentage: {match_score}%\n{message}",
        fg="#004d99"
    )

# -------------------------------
# UI Elements
# -------------------------------

# Heading
heading = Label(
    root,
    text="💫 Match Calculator 💫",
    font=("Comic Sans MS", 16, "bold"),
    bg="#e6f2ff",
    fg="#004d99"
)
heading.pack(pady=15)

# First Name
slot1 = Label(root, text="Enter Your Name:", font=("Arial", 11), bg="#e6f2ff")
slot1.pack()
name1 = Entry(root, border=3, font=("Arial", 11), width=30)
name1.pack(pady=5)

# Second Name
slot2 = Label(root, text="Enter Other Person's Name:", font=("Arial", 11), bg="#e6f2ff")
slot2.pack()
name2 = Entry(root, border=3, font=("Arial", 11), width=30)
name2.pack(pady=5)

# Calculate Button
calc_btn = Button(
    root,
    text="Calculate Match 🔮",
    command=calculate_match,
    bg="#3399ff",
    fg="white",
    font=("Arial", 11, "bold"),
    width=17,
    height=2,
    relief="raised",
    bd=3
)
calc_btn.pack(pady=15)

# Result Label
result_label = Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    bg="#e6f2ff",
    fg="#004d99",
    justify="center"
)
result_label.pack(pady=10)

# Footer
footer = Label(
    root,
    text="✨ Match Calculator using Python Tkinter ✨",
    font=("Arial", 9, "italic"),
    bg="#e6f2ff",
    fg="#005580"
)
footer.pack(side="bottom", pady=10)

# Run the app
root.mainloop()
