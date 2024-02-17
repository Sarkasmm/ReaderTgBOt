from services.file_handling import book

class User:
    def __init__(self, user_id):
        self.user_id = user_id
        self.page = 1
        self.bookmarks = set()

    def append_bookmarks(self):
        self.bookmarks.add(self.page)

    def delete_bookmarks(self, bookmark):
        self.bookmarks.remove(bookmark)

    def next_page(self):
        self.page += 1

    def previous_page(self):
        if self.page > 0:
            self.page -= 1

    def get_current_page(self):
        return book[self.page]

users_db: dict[int, User] = {}

def create_user(user_id):
    if user_id not in users_db:
        users_db[user_id] = User(user_id)


