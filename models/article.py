from database.connection import get_db_connection  # Assuming this is where db connection is set up
class Article:
    def __init__(self, id:int, title:str, content:str, author_id:int, magazine_id:int):
        if not isinstance(title,str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters.")
        if not isinstance(content,str) or len(content) == 0:
            raise ValueError("Content cannot be empty.")
        
        conn = get_db_connection()
        cursor = conn.cursor()
    # Insert the new article into the database if `id` is None
        if id is None:
         cursor.execute(
            "INSERT INTO articles (title, content, author_id, magazine_id) VALUES (?, ?, ?, ?)",
            (title, content, author_id, magazine_id)
        )
         self.id = cursor.lastrowid
        else:
         self.id = id

        conn.commit()
        conn.close()

        self.id = id
        self.title = title
        self.content = content
        self.author_id = author_id
        self.magazine_id = magazine_id

    def __repr__(self):
        return f'<Article {self.title}>'
    @property
    def title(self):
        if not hasattr(self, '_title'):  # Check if the title is already loaded
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT title FROM articles WHERE id = ?", (self.id,))
            title = cursor.fetchone()["title"]
            conn.close()
            self._title = title  # Store the title in _title
        return self._title
    # Setter for title
    @title.setter
    def title(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Title must be a non-empty string.")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE articles SET title = ? WHERE id = ?", (value, self.id))
        conn.commit()
        conn.close()
        self._title = value  # Store the updated title in _title

    @property
    def content(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT content FROM articles WHERE id = ?", (self.id,))
        content = cursor.fetchone()["content"]
        conn.close()
        return content

    @content.setter
    def content(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Content cannot be empty.")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE articles SET content = ? WHERE id = ?", (value, self.id))
        conn.commit()
        conn.close()

    def author(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT authors.* FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.id = ?
        """, (self.id,))
        author = cursor.fetchone()
        conn.close()
        return author

    def magazine(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT magazines.* FROM magazines
            JOIN articles ON magazines.id = articles.magazine_id
            WHERE articles.id = ?
        """, (self.id,))
        magazine = cursor.fetchone()
        conn.close()
        return magazine
    @classmethod
    def all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles")
        articles = cursor.fetchall()
        conn.close()
        return [cls(article["id"], article["title"], article["content"], 
                    article["author_id"], article["magazine_id"]) for article in articles]
    def delete(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM articles WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()