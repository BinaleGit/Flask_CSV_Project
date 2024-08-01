from flask import Flask, render_template
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    """
    Render the index page with data from the CSV file.
    """
    data = []
    csv_file_path = os.path.join(os.path.dirname(__file__), 'data.csv')
    with open(csv_file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
