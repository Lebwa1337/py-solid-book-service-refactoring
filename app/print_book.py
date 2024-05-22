from abc import ABC, abstractmethod

from app.book import Book


class AbstractPrintBook(ABC):

    @abstractmethod
    def print_book(self) -> None:
        pass


class ConsoleBookPrint(AbstractPrintBook):

    def __init__(self, book: Book) -> None:
        self.book = book

    def print_book(self) -> None:
        print(f"Printing the book: {self.book.title}...")
        print(self.book.content)


class ReverseBookPrint(AbstractPrintBook):
    def __init__(self, book: Book) -> None:
        self.book = book

    def print_book(self) -> None:
        print(f"Printing the book in reverse: {self.book.title}...")
        print(self.book.content[::-1])
