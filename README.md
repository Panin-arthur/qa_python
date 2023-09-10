1. test_add_new_book: Проверяет, что метод add_new_book корректно добавляет новую книгу в словарь books_genre.

2. test_add_new_book_duplicate: Проверяет, что метод add_new_book не допускает добавление дубликата книги, оставляя только одну запись.

3. test_add_new_book_invalid_name: Проверяет, что метод add_new_book не допускает добавление книги с слишком длинным названием.

4. test_set_book_genre: Проверяет, что метод set_book_genre устанавливает жанр книги, если она уже существует и указанный жанр существует в списке доступных жанров.

5. test_get_books_with_specific_genre: Проверяет, что метод get_books_with_specific_genre возвращает список книг с определенным жанром.

6. test_get_books_for_children: Проверяет, что метод get_books_for_children возвращает список книг, подходящих для детей (жанр книги не имеет возрастного рейтинга).

7. test_add_book_in_favorites: Проверяет, что метод add_book_in_favorites добавляет книгу в список избранных, если она существует в словаре books_genre.

8. test_add_book_in_favorites_duplicate: Проверяет, что метод add_book_in_favorites не допускает добавление дубликата книги в список избранных.

9. test_delete_book_from_favorites: Проверяет, что метод delete_book_from_favorites удаляет книгу из списка избранных, если она там есть.

10. test_get_books_genre: Проверяет, что метод get_books_genre возвращает текущий словарь books_genre.
