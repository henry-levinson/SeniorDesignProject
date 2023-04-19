from flask import Flask, render_template, request
from flask_paginate import Pagination, get_page_args
import psycopg2
from database_querying import DbHandler

app = Flask(__name__)

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="flask_db",
    user="postgres",
    password="123"
)

# Create an instance of the DbHandler class
db_handler = DbHandler(conn)

# Retrieve the data from the database
cur = conn.cursor()
cur.execute("SELECT * FROM \"PROTEIN_INFO\"")
protein_data = cur.fetchall()

cur.execute("SELECT * FROM \"PUBLICATION_INFO\"")
publication_data = cur.fetchall()

total = len(protein_data)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/base', methods=['GET'])
def base():
    search = request.args.get('search', '') # Get the search query from the form submission
    page = request.args.get('page', type=int, default=1)
    per_page = request.args.get('per_page', type=int, default=10)
    offset = (page - 1) * per_page

    if search:
        # Call the searchTarget function with the search query to get filtered data
        filtered_data = db_handler.searchTarget(search)
        total_results = len(filtered_data)
        pagination_data = filtered_data[offset: offset + per_page]
    else:
        # Get the full database
        filtered_data = protein_data
        total_results = len(filtered_data)
        pagination_data = filtered_data[offset: offset + per_page]

    pagination = Pagination(page=page, per_page=per_page, total=total_results,
                            css_framework='bootstrap4')

    return render_template('base.html', base=pagination_data, pagination=pagination, search=search)

@app.route('/publications')
def publications():
    search = request.args.get('search', '') # Get the search query from the form submission
    page = request.args.get('page', type=int, default=1)
    per_page = request.args.get('per_page', type=int, default=10)
    offset = (page - 1) * per_page

    if search:
        # Call the searchTarget function with the search query to get filtered data
        filtered_data = db_handler.searchTarget(search)
        total_results = len(filtered_data)
        pagination_data = filtered_data[offset: offset + per_page]
    else:
        # Get the full database
        filtered_data = publication_data
        total_results = len(filtered_data)
        pagination_data = filtered_data[offset: offset + per_page]

    pagination = Pagination(page=page, per_page=per_page, total=total_results,
                            css_framework='bootstrap4')

    return render_template('publications.html', base=pagination_data, pagination=pagination, search=search)

@app.route('/guide')
def guide():
    return render_template('guide.html')

if __name__ == '__main__':
    app.run(debug=True)