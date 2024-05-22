import json
import xml.etree.ElementTree as ET
from abc import ABC, abstractmethod

from app.book import Book


class AbstractSerializer(ABC):

    @abstractmethod
    def serialize(self):
        pass


class JSONSerializer(AbstractSerializer):

    def __init__(self, book: Book):
        self.book = book

    def serialize(self):
        return json.dumps({"title": self.book.title, "content": self.book.content})


class XMLSerializer(AbstractSerializer):
    def __init__(self, book: Book):
        self.book = book

    def serialize(self):
        root = ET.Element("book")
        title = ET.SubElement(root, "title")
        title.text = self.book.title
        content = ET.SubElement(root, "content")
        content.text = self.book.content
        return ET.tostring(root, encoding="unicode")