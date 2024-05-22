from abc import ABC, abstractmethod

from app.book import Book


class AbstractBookDisplay(ABC):

    @abstractmethod
    def display(self):
        pass


class DisplayConsole(AbstractBookDisplay):
    def __init__(self, book: Book):
        self.book = book

    def display(self):
        print(self.book.content)


class DisplayReverse(AbstractBookDisplay):
    def __init__(self, book: Book):
        self.book = book

    def display(self):
        print(self.book.content[::-1])
