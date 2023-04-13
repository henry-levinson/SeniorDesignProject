from flask import Flask, render_template, request
from flask_paginate import Pagination, get_page_args
import psycopg2

app = Flask(__name__)

# Connect to the PostgreSQL database
conn = psycopg2.connect(
    host="localhost",
    database="flask_db",
    user="postgres",
    password="123"
)

# Retrieve the data from the database
cur = conn.cursor()
cur.execute("SELECT * FROM \"PROTEIN_INFO\"")
data = cur.fetchall()
total = len(data)

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

    # Filter the data based on the search query
    filtered_data = [row for row in data if search.lower() in ' '.join(str(item) for item in row).lower()]

    pagination_data = filtered_data[offset: offset + per_page]
    pagination = Pagination(page=page, per_page=per_page, total=len(filtered_data),
                            css_framework='bootstrap4')

    return render_template('base.html', base=pagination_data, pagination=pagination, search=search)

@app.route('/guide')
def guide():
    return render_template('guide.html')

if __name__ == '__main__':
    app.run(debug=True)
