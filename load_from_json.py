import json
from pathlib import Path

def load_authors(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        for author_data in data:
            author = Author(
                fullname=author_data['fullname'],
                born_date=author_data['born_date'],
                born_location=author_data['born_location'],
                description=author_data['description']
            )
            author.save()

def load_quotes(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
        for quote_data in data:
            author = Author.objects(fullname=quote_data['author']).first()
            if author:
                quote = Quote(
                    tags=quote_data['tags'],
                    author=author,
                    quote=quote_data['quote']
                )
                quote.save()

# Load authors and quotes
load_authors(Path("authors.json"))
load_quotes(Path("quotes.json"))
