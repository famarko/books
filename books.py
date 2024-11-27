import csv
import os

#Функция для создания файла и записи данных в него
def create_file(filename, data):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        fieldnames = ['автор', 'название книги', 'тираж', 'цена', 'год издания']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            writer.writerow(item)

#Функция для чтения данных из файла
def read_books_from_file(filename):
    with open(filename, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        books = list(reader)
    return books

#Функция для вывода информации о книгах с ключевым словом в названии
def print_books_with_keyword(books, keyword):
    print(f"Книги с ключевым словом '{keyword}' в названии:")
    for book in books:
        if keyword.lower() in book['название книги'].lower():
            print(book)

#Функция для снижения цены книг до 2015 года на 10%
def reduce_price_of_old_books(books):
    for book in books:
        if int(book['год издания']) <= 2015:
            book['цена'] = str(float(book['цена']) * 0.9)

#Функция для сортировки книг по убыванию тиража
def sort_books_by_print_run(books):
    sorted_books = sorted(books, key=lambda x: int(x['тираж']), reverse=True)
    return sorted_books

#Функция для ввода данных о книгах пользователем
def input_books():
    books = []
    while True:
        author = input("Введите имя автора (или нажмите Enter для завершения ввода): ")
        if not author:
            break
        title = input("Введите название книги: ")
        print_run = input("Введите тираж книги: ")
        price = input("Введите цену экземпляра книги: ")
        year = input("Введите год издания книги: ")
        books.append({'автор': author, 'название книги': title, 'тираж': print_run, 'цена': price, 'год издания': year})
    return books

#Основная функция
def main():
    filename = 'books.csv'

    #Если файл не существует, создаем его и запрашиваем данные о книгах у пользователя
    if not os.path.exists(filename):
        books = input_books()
        create_file(filename, books)

    #Чтение данных о книгах из файла
    books = read_books_from_file(filename)

    #1. Вывод информации о книгах с ключевым словом в названии
    print_books_with_keyword(books, 'повесть')

    #2. Снижение цены книг до 2015 года на 10%
    reduce_price_of_old_books(books)

    #3. Сортировка книг по убыванию тиража
    sorted_books = sort_books_by_print_run(books)
    print("\nКниги, отсортированные по убыванию тиража:")
    for book in sorted_books:
        print(book)

if __name__ == "__main__":
    main()
