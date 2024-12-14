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

    