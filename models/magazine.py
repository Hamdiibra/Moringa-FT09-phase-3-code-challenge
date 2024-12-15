from database.connection import get_db_connection
class Magazine:
    def __init__(self, id: int, name: str, category: str):
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")

        conn = get_db_connection()
        cursor = conn.cursor()

        # Insert into the database if ID is None, otherwise set the existing ID
        if id is None:
            cursor.execute(
                "INSERT INTO magazines (name, category) VALUES (?, ?)",
                (name, category)
            )
            self.id = cursor.lastrowid
        else:
            self.id = id

        conn.commit()
        conn.close()

        self._name = name
        self._category = category

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
        return self._name

    # Setter for name
    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters.")
        self._name = value

    # Getter for category
    @property
    def category(self):
        return self._category

    # Setter for category
    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    # Method to get all articles associated with the magazine
    def articles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT articles.* FROM articles
            JOIN magazines ON articles.magazine_id = magazines.id
            WHERE magazines.id = ?
        """, (self.id,))
        articles = cursor.fetchall()
        conn.close()
        return articles  # You may want to return instances of an Article class

    # Method to get all contributors (authors) associated with the magazine
    def contributors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT authors.* FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
        """, (self.id,))
        contributors = cursor.fetchall()
        conn.close()
        return contributors  # You may want to return instances of an Author class

    # Method to get all article titles for the magazine
    def article_titles(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT title FROM articles
            WHERE magazine_id = ?
        """, (self.id,))
        titles = [row["title"] for row in cursor.fetchall()]
        conn.close()
        return titles if titles else None

    # Method to get authors who have written more than 2 articles for the magazine
    def contributing_authors(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT authors.*, COUNT(articles.id) AS article_count FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
            GROUP BY authors.id
            HAVING article_count > 2
        """, (self.id,))
        authors = cursor.fetchall()
        conn.close()
        return authors if authors else None
    @classmethod
    def all(cls):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines")
        magazines = cursor.fetchall()
        conn.close()
        return [cls(magazine["id"], magazine["name"], magazine["category"]) for magazine in magazines]
    def delete(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM magazines WHERE id = ?", (self.id,))
        conn.commit()
        conn.close()