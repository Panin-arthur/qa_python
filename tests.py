import unittest
import pytest

class TestBooksCollector(unittest.TestCase):

    def setUp(self):
        self.collector = BooksCollector()

    def test_add_new_book(self):
        self.collector.add_new_book("Книга1")
        self.assertTrue("Книга1" in self.collector.get_books_genre())

    def test_add_new_book_duplicate(self):
        self.collector.add_new_book("Книга1")
        self.collector.add_new_book("Книга1")  # Попытка добавить дубликат
        self.assertEqual(len(self.collector.get_books_genre()), 1)  # Должна быть только одна запись

    def test_add_new_book_invalid_name(self):
        self.collector.add_new_book("Книга с очень длинным названием, которое превышает 40 символов")  # Слишком длинное название
        self.assertFalse("Книга с очень длинным названием, которое превышает 40 символов" in self.collector.get_books_genre())

    def test_set_book_genre(self):
        self.collector.add_new_book("Книга1")
        self.collector.set_book_genre("Книга1", "Фантастика")
        self.assertEqual(self.collector.get_book_genre("Книга1"), "Фантастика")

    def test_get_books_with_specific_genre(self):
        self.collector.add_new_book("Книга1")
        self.collector.set_book_genre("Книга1", "Фантастика")
        self.collector.add_new_book("Книга2")
        self.collector.set_book_genre("Книга2", "Детективы")
        books = self.collector.get_books_with_specific_genre("Фантастика")
        self.assertListEqual(books, ["Книга1"])

    def test_get_books_for_children(self):
        self.collector.add_new_book("Книга1")
        self.collector.set_book_genre("Книга1", "Фантастика")
        self.collector.add_new_book("Книга2")
        self.collector.set_book_genre("Книга2", "Детективы")
        self.collector.add_new_book("Книга3")
        self.collector.set_book_genre("Книга3", "Ужасы")
        books = self.collector.get_books_for_children()
        self.assertListEqual(books, ["Книга1"])

    def test_add_book_in_favorites(self):
        self.collector.add_new_book("Книга1")
        self.collector.add_book_in_favorites("Книга1")
        self.assertEqual(len(self.collector.get_list_of_favorites_books()), 1)

    def test_add_book_in_favorites_duplicate(self):
        self.collector.add_new_book("Книга1")
        self.collector.add_book_in_favorites("Книга1")
        self.collector.add_book_in_favorites("Книга1")  # Попытка добавить дубликат
        self.assertEqual(len(self.collector.get_list_of_favorites_books()), 1)  # Должна быть только одна избранная книга

    def test_delete_book_from_favorites(self):
        self.collector.add_new_book("Книга1")
        self.collector.add_book_in_favorites("Книга1")
        self.collector.delete_book_from_favorites("Книга1")
        self.assertEqual(len(self.collector.get_list_of_favorites_books()), 0)

    @unittest.expectedFailure  # Ожидаемое несоответствие
    def test_get_books_genre(self):
        self.collector.add_new_book("Книга1")
        self.collector.set_book_genre("Книга1", "Фантастика")
        self.assertDictEqual(self.collector.get_books_genre(), {"Книга1": "Фантастика"})

    @unittest.expectedFailure  # Ожидаемое несоответствие
    def test_get_books_genre(self):
        self.collector.add_new_book("Книга1")
        self.collector.set_book_genre("Книга1", "Фантастика")
        self.assertDictEqual(self.collector.get_books_genre(), {"Книга1": "Фантастика"})

    @pytest.mark.parametrize("book_name, genre", [("Книга1", "Фантастика"), ("Книга2", "Детективы")])
    def test_set_book_genre_update(self, book_name, genre):
        self.collector.add_new_book(book_name)
        self.collector.set_book_genre(book_name, genre)
        self.assertEqual(self.collector.get_book_genre(book_name), genre)

if __name__ == '__main__':
    unittest.main()