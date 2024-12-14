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
