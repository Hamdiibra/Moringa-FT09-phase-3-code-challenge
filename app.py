from database.setup import create_tables
from database.connection import get_db_connection
from models.article import Article
from models.author import Author
from models.magazine import Magazine

def main():
    # Initialize the database and create tables
    create_tables()

    # Collect user input
    author_name = input("Enter author's name: ")
    magazine_name = input("Enter magazine name: ")
    magazine_category = input("Enter magazine category: ")
    article_title = input("Enter article title: ")
    article_content = input("Enter article content: ")

    # Connect to the database
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        # Start a transaction (implicitly handled by SQLite with commit)
        conn.execute('BEGIN TRANSACTION')

        # Create an author instance (the name is validated in the Author class constructor)
        author = Author(id=None, name=author_name)  # ID is None for new author
        print(f"Author '{author.name}' added successfully.")

        # Create a magazine instance (the name and category are validated in the Magazine class constructor)
        magazine = Magazine(id=None, name=magazine_name, category=magazine_category)  # ID is None for new magazine
        print(f"Magazine '{magazine.name}' added successfully.")

        # Create an article instance (ID is None for new article)
        article = Article(id=None, title=article_title, content=article_content, 
                          author_id=author.id, magazine_id=magazine.id)  # Validate foreign keys for author and magazine
        print(f"Article '{article.title}' added successfully.")

        # Commit the transaction
        conn.commit()

        # Fetch the latest data to display (use class methods instead of raw SQL queries)
        print("\nFetching all authors, magazines, and articles:")

        # Display all magazines, authors, and articles using the class methods
        print("\nMagazines:")
        for magazine in Magazine.all():  # Assuming you have a method `all()` in the Magazine class
            print(magazine)

        print("\nAuthors:")
        for author in Author.all():  # Assuming you have a method `all()` in the Author class
            print(author)

        print("\nArticles:")
        for article in Article.all():  # Assuming you have a method `all()` in the Article class
            print(article)

    except Exception as e:
        # Rollback in case of any error
        conn.rollback()
        print(f"An error occurred: {e}")

    finally:
        # Always close the connection
        conn.close()

if __name__ == "__main__":
    main()
