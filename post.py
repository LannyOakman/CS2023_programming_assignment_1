from datetime import datetime
class Post:

    post_count = 0

    def __init__(self, author, content, tags=None):

        if not Post.is_valid_content(content):
            raise ValueError("Invalid Post Content.")
        
        self._author = author
        self._content = content

        if tags:
            for tag in tags:
                if not Post.is_valid_tag(tag):
                    raise ValueError("Invalid Tag.")
            self._tags = set(tags)
        else:
            self._tags = set()
        
        self._created_on = datetime.now()
        self._liked_by = list()
        self._comments = list()

        Post.post_count += 1

    @property
    def content(self):
        return self._content
    
    @property
    def created_on(self):
        return self._created_on
    
    @property
    def tags(self):
        return self._tags
    
    @property
    def liked_by(self):
        return self._liked_by

    def add_tag(self, tag):
        if not Post.is_valid_tag(tag):
            raise ValueError("Invalid tag")
        self._tags.add(tag)

    def remove_tag(self, tag):
        self._tags.discard(tag)

    @classmethod
    def get_post_count(cls):
        return cls.post_count

    @staticmethod
    def is_valid_content(content):
        if not(3 <= len(content) <= 2200):
            return False
        return True

    @staticmethod
    def is_valid_tag(tag: str):
        if not (tag.isalnum() and len(tag) <= 30):
            return False
        return True