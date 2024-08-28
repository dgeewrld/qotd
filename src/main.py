from quotes import load_quotes
from display import show_quote
import os

def main():
    # Load quotes from CSV
    file_path = os.path.join(os.path.dirname(__file__), '..', 'quotes.csv')
    quotes = load_quotes(file_path)

    # Show the quote of the day app
    show_quote(quotes)

if __name__ == "__main__":
    main()
