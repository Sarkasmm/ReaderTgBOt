import sys
import os

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1000

book: dict[int, str] = {}
def prepare_book(path: str) -> None:
    page = 1
    with open(path, 'r', encoding='UTF-8') as file:
        text = file.read()
        start = 0
        end = len(text)
        while start < end:
            page_text, current_page_size = _get_part_text(text, start, PAGE_SIZE)
            start += current_page_size + 1
            book[page] = page_text.lstrip()
            page += 1

def _get_part_text(text, start, page_size):
    end = start + page_size - 1
    stop = ',!?.:;'
    while len(text) > end and (text[end] not in stop or text[end] in stop and (text[end-1] in stop or text[end+1] in stop)):
        end -= 1
    return text[start:end + 1], len(text[start:end + 1])

prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))