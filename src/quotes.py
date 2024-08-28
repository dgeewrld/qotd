import pandas as pd
import random

def load_quotes(file_path):
    """
    Load quotes and authors from a CSV file.
    :param file_path: Path to the CSV file containing quotes and authors.
    :return: List of dictionaries with 'quote' and 'author'.
    """
    df = pd.read_csv(file_path)
    quotes = df.to_dict(orient='records')  # Convert each row to a dictionary
    return quotes

def get_random_quote(quotes):
    """
    Select a random quote from the list of quotes.
    :param quotes: List of dictionaries with 'quote' and 'author'.
    :return: A randomly selected dictionary with 'quote' and 'author'.
    """
    return random.choice(quotes)
