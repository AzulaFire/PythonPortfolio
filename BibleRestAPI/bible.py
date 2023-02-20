import pandas as pd


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




df = pd.read_json(f"BIBLE/Popular.json")
total = len(df) - 1

print(df["book"][97], df["chapter"][97], df["verse"][97])

