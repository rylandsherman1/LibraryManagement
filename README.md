# Library Management System

# Creators

# Ryland Sherman

LinkedIn: https://www.linkedin.com/in/ryland-sherman-80a1a72a2/
Github: https://github.com/rylandsherman1

# Kimberly Palmer

LinkedIn: https://www.linkedin.com/in/kimberly-l-palmer/
Github: https://github.com/kimberlylpalmer

# Overview

This Library Management System is a Python CLI application designed to manage a library's books, members, and borrowing records. It uses SQLAlchemy for database operations and provides a user-friendly interface to interact with the library's data.

# Features

Manage Books: Add, delete, view, and find books.

Manage Members: Register, delete, view, and find library members.

Manage Borrow Records: Create and delete borrow records, view all records, and track books borrowed by members and vice versa.

# Installation

To run this application, you need Python installed on your system. If you don't have Python installed, download and install it from python.org.

# Clone the Repository

Copy code

git clone git@github.com:rylandsherman1/LibraryManagement.git

cd LibraryManagement

code .

# Install Dependencies

pipenv install

pipenv shell

pip install sqlalchemy

# Usage

run the application using Python:
python -m lib.app

# CLI Options

# Manage Books:

Add a new book.
Delete an existing book.
View all books.
Find a book by ISBN, title, or author.

# Manage Members:

Add a new member.
Delete an existing member.
View all members.
Find a member by membership number, name, or email.

# Manage Borrow Records:

Create a new borrow record.
Delete an existing borrow record.
View all borrow records.
View books borrowed by a specific member.
View members who borrowed a specific book.

# Testing

The application should be manually tested by running through all the CLI options and ensuring that each functionality works as expected. Make sure to test edge cases such as:

Adding a book/member with existing details.
Deleting a book/member that doesn't exist.
Borrowing operations with invalid book or member IDs.

# Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.
