import json
import xml.etree.ElementTree as et

class Book:
    def __init__(self, bookid,booktitle,bookauthor):
        self.bookid = bookid
        self.booktitle = booktitle
        self.bookauthor = bookauthor

class BookSerializer:
    def serialize(self,book,format):
        serializer = get_serializer(format)
        return serializer(book)

def get_serializer(format):
    if format == 'JSON':
        return _serialize_to_json
    if format == 'XML':
        return _serialize_to_xml

def _serialize_to_json(book):
    payload = {
        'bookid': book.bookid,
        'booktitle': book.booktitle,
        'bookauthor': book.bookauthor
    }
    return json.dumps(payload)

def _serialize_to_xml(book):
    book_element = et.Element('book',attrib={'bookid': str(book.bookid)})
    title = et.SubElement(book_element, 'title')
    title.text = book.booktitle
    author = et.SubElement(book_element,'author')
    author.text = book.bookauthor
    return et.tostring(book_element, encoding='unicode')

if __name__ == '__main__':
    book = Book(1,'programming in ruby','matz')
    serializer = BookSerializer()
    result = serializer.serialize(book,'XML')
    print(result)
