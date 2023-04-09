from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/base')
def base():
    # Read data from file
    df = pd.read_csv('data.csv')
    # Convert dataframe to list of rows
    dataframe = df.values.tolist()
    return render_template('base.html', dataframe=dataframe)

@app.route('/guide')
def guide():
    return render_template('guide.html')

if __name__ == '__main__':
    app.run(debug=True)
