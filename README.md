# Books Manager

Books Manager is a simple command-line application that allows you to manage a list of books. It lets you add, lookup, and display books using an SQLite database for data storage.

## Features

- **Add a Book**: Add a new book with the name, author, and number of pages.
- **Lookup a Book**: Search for books by name, author, or number of pages.
- **Display Books**: Display all books in the database in a formatted table.
- **Persistent Storage**: Stores the books data in an SQLite database.

## Requirements

- Python 3.x
- SQLite3

## Live videocast
https://drive.google.com/file/d/1SuJGMuRZBfTPYW6u-D4K6HelnrpYMqM0/view?usp=sharing

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/books-manager.git
    cd books-manager
    ```

2. **Create a virtual environment (optional but recommended)**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies**:
    This project does not have any external dependencies beyond Python's standard library.

## Usage

1. **Run the application**:
    ```sh
    python main.py
    ```

2. **Interact with the Books Manager**:
    - You will be presented with a menu with the following options:
        ```
        ***Books Manager***
        1) Add a book
        2) Lookup a book
        3) Display books
        4) Quit
        ```

3. **Add a Book**:
    - Choose option `1` and enter the book details when prompted.

4. **Lookup a Book**:
    - Choose option `2` and enter a search term. The application will display all matching books.

5. **Display Books**:
    - Choose option `3` to display all books in the database.

6. **Quit**:
    - Choose option `4` to quit the application.

## Project Structure

- `main.py`: The main script that runs the Books Manager application.

## Database

The application uses SQLite for data storage. The database file `books.db` will be created in the project directory if it does not already exist. The `books` table will be created with the following schema:

```sql
CREATE TABLE IF NOT EXISTS books (
    name TEXT,
    author TEXT,
    pages INTEGER
);
