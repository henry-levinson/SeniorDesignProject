from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/base')
def base():
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(
        host="localhost",
        database="flask_db",
        user="postgres",
        password="123")

    # Retrieve the data from the database
    cur = conn.cursor()
    cur.execute("SELECT * FROM \"PROTEIN_INFO\"")
    data = cur.fetchall()

    # Calculate offset based on current page number and rows per page
    page_number = 1  # Replace with actual page number
    rows_per_page = 25  # Replace with actual rows per page
    offset = (page_number - 1) * rows_per_page

    # Define limit as number of rows per page
    limit = rows_per_page

    # Calculate start and stop values based on offset and limit
    start = offset
    stop = offset + limit

    # Create the context dictionary
    context = {'base': data, 'start': start, 'stop': stop}

    # Render the template and pass in the context dictionary
    return render_template('base.html', **context)


@app.route('/guide')
def guide():
    return render_template('guide.html')

if __name__ == '__main__':
    app.run(debug=True)
