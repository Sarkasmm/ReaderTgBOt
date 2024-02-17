class Users:
    users_db = {}

    def __init__(self, user_id):
        if user_id not in self.users_db:
            self.user_id = user_id
            self.page = 0
            self.bookmarks = set()

    def append_bookmarks(self, bookmark):
        self.users_db[self.user_id]] = 0

