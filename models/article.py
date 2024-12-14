class Article:
    def __init__(self, id:int, title:str, content:str, author_id:int, magazine_id:int):
        if not isinstance(title,str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters.")
        if not isinstance(content,str) or len(content) == 0:
            raise ValueError("Content cannot be empty.")
        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self):
        return f'<Article {self.title}>'
    #Getter for id
    @property
    def id(self):
        return self._id
    #Getter for title
    @property
    def title(self):
        return self._title
    # Getter for content
    @property
    def content(self):
        return self._content
    # Getter for author_id
    @property
    def author_id(self):
        return self._author_id

    # Getter for magazine_id
    @property
    def magazine_id(self):
        return self._magazine_id