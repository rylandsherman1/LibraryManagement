# Library Management System

## Table of Contents:

1. [Creators](#creators)
2. [Overview](#overview)
3. [Features](#features)
4. [Installation](#installation)
5. [Clone the Repository](#clone)
6. [Install Dependencies](#install)
7. [Usage](#usage)
8. [CLI Options](#cli)
9. [Testing](#testing)
10. [Contributing](#contributing)
11. [License](#license)

# Creators

# Ryland Sherman

LinkedIn: https://www.linkedin.com/in/ryland-sherman-80a1a72a2/
Github: https://github.com/rylandsherman1

# Kimberly Palmer

LinkedIn: https://www.linkedin.com/in/kimberly-l-palmer/
Github: https://github.com/kimberlylpalmer

[Back to Table of contents](#table-of-contents)

# Overview

This Library Management System is a Python CLI application designed to manage a library's books, members, and borrowing records. It uses SQLAlchemy for database operations and provides a user-friendly interface to interact with the library's data.

[Back to Table of contents](#table-of-contents)

# Features

Manage Books: Add, delete, view, and find books.

Manage Members: Register, delete, view, and find library members.

Manage Borrow Records: Create and delete borrow records, view all records, and track books borrowed by members and vice versa.

[Back to Table of contents](#table-of-contents)

# Installation

To run this application, you need Python installed on your system. If you don't have Python installed, download and install it from python.org.

[Back to Table of contents](#table-of-contents)

# Clone the Repository

Copy code

git clone git@github.com:rylandsherman1/LibraryManagement.git

cd LibraryManagement

code .

[Back to Table of contents](#table-of-contents)

# Install Dependencies

pipenv install

pipenv shell

pip install sqlalchemy

[Back to Table of contents](#table-of-contents)

# Usage

run the application using Python:
python -m lib.app

[Back to Table of contents](#table-of-contents)

# CLI Options

# Manage Books:

Add a new book.
Delete an existing book.
View all books.
Find a book by ISBN, title, or author.

[Back to Table of contents](#table-of-contents)

# Manage Members:

Add a new member.
Delete an existing member.
View all members.
Find a member by membership number, name, or email.

[Back to Table of contents](#table-of-contents)

# Manage Borrow Records:

Create a new borrow record.
Delete an existing borrow record.
View all borrow records.
View books borrowed by a specific member.
View members who borrowed a specific book.

[Back to Table of contents](#table-of-contents)

# Testing

The application should be manually tested by running through all the CLI options and ensuring that each functionality works as expected. Make sure to test edge cases such as:

Adding a book/member with existing details.
Deleting a book/member that doesn't exist.
Borrowing operations with invalid book or member IDs.

[Back to Table of contents](#table-of-contents)

# Contributing

Contributions to this project are welcome. Please fork the repository and submit a pull request with your changes.

[Back to Table of contents](#table-of-contents)

# License

The MIT License (MIT)

Copyright (c) 2023 The Library Management System - Phase 3

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files ("Library Management System"), to deal in Library Management System without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of Library Management System, and to permit persons to whom Library Management System is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of Library Management System.

LIBRARY MANAGEMENT SYSTEM IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITHLIBRARY MANAGEMENT SYSTEM OR THE USE OR OTHER DEALINGS IN LIBRARY MANAGEMENT SYSTEM.

[Back to Table of contents](#table-of-contents)
