import csv

books = []

class Book:
    def __init__(self, title: str, author: str, original_lang: str, first_pub: int, sales_in_mil: float, genre: str):
        self.title = title
        self.author = author
        self.original_lang = original_lang
        self.first_pub = first_pub
        self.sales_in_mil = sales_in_mil
        self.genre = genre

    def __str__(self):
        return f"{self.title}, {self.original_lang}, {self.first_pub}, {self.sales_in_mil}, {self.genre}"

with open("Bestseller.csv", "r", encoding="utf-8") as file:
    csv_reader = csv.reader(file)

    for i, value in enumerate(csv_reader):
        if i == 0:
            continue
        else:
            books.append(Book(value[0], value[1], value[2], int(value[3]), float(value[4]), value[5]))

for book in books:
    print(str(book))

highest_sales = 0
i = 0

for index, value in enumerate(books):
    if value.sales_in_mil > highest_sales:
        highest_sales = value.sales_in_mil
        i = index

print(f"Highest Sales: {highest_sales} millions")
print(f"Highest Sales is {books[i].title} by {books[i].author}")

with open("bestseller_info.csv", "w") as file:
    csv_writer = csv.writer(file)

    csv_writer.writerow([books[i].title, books[i].author, books[i].original_lang, books[i].first_pub, books[i].sales_in_mil, books[i].genre])