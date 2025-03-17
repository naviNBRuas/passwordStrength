'''
This is the main file of the password strength testing tool.
It provides a user-friendly interface for users to evaluate the strength of their passwords.
'''
import tkinter as tk
from password_strength import PasswordStrength
class PasswordStrengthApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Strength Tester")
        self.password_label = tk.Label(root, text="Enter your password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(root, show="*")
        self.password_entry.pack()
        self.check_button = tk.Button(root, text="Check Strength", command=self.check_strength)
        self.check_button.pack()
        self.strength_label = tk.Label(root, text="")
        self.strength_label.pack()
        self.suggestions_label = tk.Label(root, text="")
        self.suggestions_label.pack()
    def check_strength(self):
        password = self.password_entry.get()
        strength = PasswordStrength.get_strength(password)
        self.strength_label.config(text=f"Password Strength: {strength}")
        suggestions = PasswordStrength.get_suggestions(password)
        self.suggestions_label.config(text=f"Suggestions: {suggestions}")
if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordStrengthApp(root)
    root.mainloop()