import tkinter as tk
from quotes import get_random_quote
import os

class QuoteApp:
    def __init__(self, root, quotes):
        self.root = root
        self.quotes = quotes

        self.root.title("Quote of the Day")

        # Center the window
        window_width = 400
        window_height = 300
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        position_top = int(screen_height/2 - window_height/2)
        position_right = int(screen_width/2 - window_width/2)
        self.root.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

        # Quote label
        self.quote_label = tk.Label(self.root, text="", wraplength=350, justify="center", padx=10, pady=10, font=('Helvetica', 12, 'italic'))
        self.quote_label.pack(expand=True)

        # Author label
        self.author_label = tk.Label(self.root, text="", wraplength=350, justify="center", padx=10, font=('Helvetica', 10, 'normal'))
        self.author_label.pack(pady=(0, 50))  # Adjust padding to move it up from the bottom

        # New Quote button
        self.new_quote_button = tk.Button(self.root, text="New Quote", command=self.display_random_quote)
        self.new_quote_button.pack(pady=10)

        # Display the first quote
        self.display_random_quote()

    def display_random_quote(self):
        """Display a randomly selected quote and author."""
        quote_data = get_random_quote(self.quotes)
        self.quote_label.config(text=f"\"{quote_data['quote']}\"")
        self.author_label.config(text=f"- {quote_data['author']}")

def show_quote(quotes):
    """Create the main application window and start the app."""
    root = tk.Tk()
    app = QuoteApp(root, quotes)
    root.mainloop()
