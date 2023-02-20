from flask import Flask, render_template
import pandas as pd
import json
import random

app = Flask(__name__)

books = pd.read_json("BIBLE/Books.json")
popular = pd.read_json("BIBLE/Popular.json")

def format_book(book):
    if book[0].isdigit():
        book = book[0] + " " + book[1:]

    book = book.split()


    if len(book) == 2:
        book_name = book[0] + " " + book[1].title()
        book = book[0] + book[1].title()
    elif len(book) == 3:
        book_name = book[0].title() + " " + book[1] + " " + book[2].title()
        book = book[0].title() + book[1] + book[2].title()
    else:
        book = book[0].title()
        book_name = book
    return book, book_name


@app.route("/")
def home():
    return render_template("home.html", data=books.to_html(), popular=popular.to_html())

@app.route("/api/v1/<book>/<chapter>/<verse>/")
def api_verse(book, chapter, verse):
    book, book_name = format_book(book)
    
    # Read the JSON file
    with open(f"BIBLE/{book}.json", "r") as f:
        data = json.load(f)

    # Convert it into a DataFrame
    df = pd.json_normalize(data, record_path=["chapters", "verses"], meta=["book", ["chapters", "chapter"]])
    df.columns = ["Verse", "Text", "Book", "Chapter"]  # rename columns

    # Query the required content
    query = f"Book == '{book_name}' and Chapter == '{chapter}' and Verse == '{verse}'"
    result = df.query(query).to_dict(orient="records")[0]

    return result

@app.route("/api/v1/<book>/<chapter>/")
def api_chapter(book, chapter):
    book, book_name = format_book(book)
    
    # Read the JSON file
    with open(f"BIBLE/{book}.json", "r") as f:
        data = json.load(f)

    # Convert it into a DataFrame
    df = pd.json_normalize(data, record_path=["chapters", "verses"], meta=["book", ["chapters", "chapter"]])
    df.columns = ["Verse", "Text", "Book", "Chapter"]  # rename columns

    # Query the required content
    query = f"Book == '{book_name}' and Chapter == '{chapter}'"
    result = df.query(query).to_dict(orient="records")

    return result


@app.route("/api/v1/random/")
def api_random():
    
    # Read the JSON file
    df = pd.read_json(f"BIBLE/Popular.json")
    total = len(df) - 1

    num = random.randrange(total)

    book = df["book"][num]
    chapter = df["chapter"][num]
    verse = df["verse"][num]

    result = api_verse(book, chapter, verse)

    return result




# Only run script if script is ran directly, not imported
if __name__ == "__main__":
    app.run(debug=True)

