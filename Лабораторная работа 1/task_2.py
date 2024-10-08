pages = 100
lines = 50
symbols = 25

disc_size_bytes = 1.44 * 1024 ** 2  # объем дискеты в байтах

symbol_count_book = symbols * lines * pages  # количество символов в одной книге
symbol_count_book_bytes = symbol_count_book * 4 # сколько байт занимает это количество символов
book_count = disc_size_bytes / symbol_count_book_bytes

print("Количество книг, помещающихся на дискету:", round(book_count))
