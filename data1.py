import requests
import sqlite3
from typing import Union

def base_de_datos():
    

    url = "https://all-books-api.p.rapidapi.com/getBooks"

    headers = {
        "X-RapidAPI-Key": "fbc615dc91mshe3a023dccd77a48p1e2f6cjsn2e2ef44125c6",
        "X-RapidAPI-Host": "all-books-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        books_data = response.json()

        # Organizar los datos en un diccionario
        books_dict = {}
        for book in books_data:
            book_id = book['id']
            books_dict[book_id] = {
                'title': book.get('title', ''),
                'author': book.get('author', ''),
                'published_year': book.get('published_year', ''),
                'genre': book.get('genre', ''),
                'description': book.get('description', ''),
            }
        for book_id, book_info in books_dict.items():
            print(f"Book ID: {book_id}")
            print(f"Title: {book_info['title']}")
            print(f"Author: {book_info['author']}")
            print(f"Published Year: {book_info['published_year']}")
            print(f"Genre: {book_info['genre']}")
            print(f"Description: {book_info['description']}")
            print("="*30)
    else:
        print("Failed to retrieve data from the API")

def create_book_database(books: dict, nombre:str) -> Union[bool, str]:
    try:
        # Conexión a la base de datos (se creará si no existe)
        conexion = sqlite3.connect(nombre)
        cursorBF = conexion.cursor()

        # Crear tabla de libros si no existe
        cursorBF.execute('''CREATE TABLE IF NOT EXISTS books
                    (title TEXT, author TEXT, categories TEXT, language TEXT, summary TEXT, isbn TEXT, cover_art_url TEXT)''')

        # Insertar los datos de los libros en la tabla
        for title, details in books.items():
            cursorBF.execute("INSERT INTO books (title, author, categories, language, summary, isbn, cover_art_url) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (title, details["author"], ", ".join(details["categories"]), details["language"], details["summary"], details["isbn"], details["cover_art_url"]))
    
        # Guardar cambios y cerrar la conexión
        conexion.commit()
        conexion.close()
        return True, ""
    except Exception as e:
        return False, e 
    



    
