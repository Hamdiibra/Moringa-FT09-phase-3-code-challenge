## Author-Article-Magazine Database System

# Project Overview:
This project is designed to manage a database system that tracks Authors, Articles, and Magazines. The system allows you to:

- Create authors and magazines
- Assign authors to articles
- Associate articles with magazines
- Query articles by author or magazine
- Get a list of contributing authors who have written more than two articles for a specific magazine

# Features
Author Management: Create and manage authors, each of whom can write multiple articles.
Article Management: Create articles, assign them to authors, and link them to magazines.
Magazine Management: Create and manage magazines, each containing multiple articles.
Dynamic Queries: Fetch authors, articles, and magazines easily with relationships defined using SQLAlchemy.
Contributing Authors: Query authors who have written more than two articles for a specific magazine.

# Prerequisites
To run this project, you need the following installed on your system:

- Python (version 3.6+)
- SQLAlchemy: Install it using pip:

```bash
pip install sqlalchemy
```
- SQLite (or any other SQL-compatible database of your choice)

# Getting Started
1. Clone the repository
First, clone this repository to your local machine:

   ```bash
git clone git@github.com:Hamdiibra/Moringa-FT09-phase-3-code-challenge.git
   ```
2. Navigate to the project directory:
   ```bash
cd Moringa-FT09-phase-3-code-challenge.git
   ```
# Next Steps

1. Error Handling

Implement error handling for database operations (e.g., missing tables, connection errors).

2. Advanced Queries

Add features like filtering by date range, sorting, and full-text search.

3. API Integration (Optional)

Use a web framework like Flask or FastAPI to expose your database functionality as an API.

4. Documentation

Expand this README with clear examples of usage, an ER diagram, and contributing guidelines.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

Feel free to reach out for support or contributions!