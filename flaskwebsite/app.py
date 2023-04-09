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
        # user=os.environ['DB_USERNAME'],
        # password=os.environ['DB_PASSWORD']
        user = "postgres",
        password = "123")

    # Retrieve the data from the database
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    data = cur.fetchall()

    # Create the context dictionary
    # context = {'my_data': data}
    context = {'base': data}

    # Render the template and pass in the context dictionary
    return render_template('base.html', **context)

@app.route('/guide')
def guide():
    return render_template('guide.html')

if __name__ == '__main__':
    app.run(debug=True)
