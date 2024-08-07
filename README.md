Financial Tracker:

A CRUD web application developed using Flask, SQLAlchemy, HTML, Jinja2, and CSS for managing and tracking personal finances. I made this software to explore backend development concepts and create a functional financial tracking tool.

Major credit to @codewithjosh on youtube who's introduction to flask and SQLalchemy was what taught me these concepts. 

Project Overview:

The Financial Tracker is a backend-focused web application that allows users to:

Create: Add new income and expense entries.

Read: View existing financial transactions and summaries.

Update: Modify or correct existing income and expense entries.

Delete: Remove income and expense entries.

This project provides hands-on experience with backend technologies, including Flask for web development and SQLAlchemy for database management. It does not include user authentication or other advanced features, and it is not intended for public use.


Prerequisites
Python 3.x
Flask
SQLAlchemy


Setup Instructions: 
1. Clone the Repository

2. Copy code
git clone https://github.com/yourusername/financial-tracker.git
cd financial-tracker

4. Create a Virtual Environment

Copy code
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


5. Install Dependencies

bash
Copy code
pip install -r requirements.txt
Configure the Database

6. Run the following command to set up the initial database schema:

flask db upgrade


7. Run the Application:

flask run

The application will be available at http://127.0.0.1:5000/.

Usage:

Add Transactions: Use the interface to create new income and expense entries.

View Transactions: Navigate through the application to view existing transactions and financial summaries.

Update Transactions: Edit or update existing income and expense entries.

Delete Transactions: Remove transactions as needed.

Project Structure

app.py: Main application file containing routes and application setup.

models.py: Contains SQLAlchemy models and database schema.

templates/: Jinja2 HTML templates.

static/: CSS files and other static assets.

migrations/: Database migration scripts.
