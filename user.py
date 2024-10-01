from datetime import datetime
import re

class User:
    user_count = 0

    def __init__(self, username: str, email: str):

        if not (User.is_valid_username(username)):
            raise ValueError("Invalid username.")
        
        if not User.is_valid_email(email):
            raise ValueError("Invalid email address.")

        self._username = username
        
        self._email = email
        self._bio = ""
        self._joined_on = datetime.now()

        self._posts = list()
        self._liked_posts = list()
        self._comments = list()
        self._liked_comments = list()

        self.following = list()
        self.followers = list()

        User.user_count += 1

    @property
    def username(self):
        return self._username
    
    @property
    def email(self):
        return self._email
    
    @property
    def bio(self):
        return self._bio

    @bio.setter
    def bio(self, new_bio: str):
        if len(new_bio) > 150:
            raise ValueError("Bio must be 150 characters or less.")
        
        self._bio = new_bio
    
    @property
    def joined_on(self):
        return self._joined_on
    
    @property
    def posts(self):
        return self._posts

    @staticmethod
    def is_valid_username(username: str) -> bool:
        if not (3 <= len(username) <= 30 ):
            return False

        char_reqs = "abcdefghijklmnopqrstuvwxyz._1234567890"

        for char in username.lower():
            if not(char in char_reqs):
                return False
        return True

    @staticmethod
    def is_valid_email(email: str):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        
        return bool(re.match(pattern, email))
    
    @classmethod
    def get_user_count(cls):
        return cls.user_count