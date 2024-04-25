import data

base_1 = data.buscar_por_categoria("Science & Technology", 100)
status, error = data.create_book_database(base_1)
if status:
    print("Libros guardados correctamente.")
else:
    print("Los libros no se pudieron guardar: ", error)






