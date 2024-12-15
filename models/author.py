from database.connection import get_db_connection
class Author:
    def __init__(self, id: int, name: str):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        
        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert into the database if ID is None, otherwise set the existing ID
        if id is None:
            cursor.execute(
                "INSERT INTO authors (name) VALUES (?)",
                (name,)
            )
            self.id = cursor.lastrowid
        else:
            self.id = id

        conn.commit()
        conn.close()

        self.name = name

    def __repr__(self):
        return f"<Author {self.name}>"
    # Getter for ID
    @property
    def id(self):
        return self._id

    # Setter for ID
    @id.setter
    def id(self, value):
        if hasattr(self, '_id'):
            raise AttributeError("ID cannot be modified once set.")
        if not isinstance(value, int):
            raise ValueError("ID must be an integer.")
        self._id = value

    # Getter for name
    @property
    def name(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM authors WHERE id = ?", (self.id,))
        name = cursor.fetchone()["name"]
        conn.close()
        return name

    # Setter for name
    @name.setter
    def name(self, value):
        if hasattr(self, '_name'):
            raise AttributeError("Name cannot be changed after the author is instantiated.")
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Name must be a non-empty string.")
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE authors SET name = ? WHERE id = ?", (value, self.id))
        conn.commit()
        conn.close()
        self._name = value

    # Method to get all articles associated with the author
    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT articles.* FROM articles
            JOIN authors ON articles.author_id = authors.id
            WHERE authors.id = ?
        """, (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles  

    # Method to get all magazines associated with the author
    def magazines(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT magazines.* FROM magazines
            JOIN articles ON articles.magazine_id = magazines.id
            WHERE articles.author_id = ?
        """, (self.id,))
        magazines = cursor.fetchall()
        conn.close()
        return magazines  
    @classmethod
    def all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors")
        authors = cursor.fetchall()
        conn.close()
        return [cls(author["id"], author["name"]) for author in authors]
    def delete(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM authors WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()