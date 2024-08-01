# Flask CSV Project

This project demonstrates how to read data from a CSV file and display it on a web page using Flask.

## Project Structure

```plaintext
flask_csv_project/
├── templates/
│   └── index.html
├── app.py
├── data.csv
├── requirements.txt
└── README.md
```
## Setup Instructions
1. Clone the Repository
```plaintext
git clone https://github.com/yourusername/flask_csv_project.git
cd flask_csv_project
```
2. Create and Activate a Virtual Environment
```plaintext
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install the Required Packages
```plaintext
pip install -r requirements.txt
```
4. Run the Application
```plaintext
python app.py
```
5. View the Application
Open your web browser and go to http://127.0.0.1:5000/ to see the data from data.csv displayed on the web page.

Project Details
-   app.py: The main application file that initializes the Flask app and handles the route to display the CSV data.
-   data.csv: The CSV file containing the data to be displayed.
-   templates/index.html: The HTML template used to render the data on the web page.
-   requirements.txt: The file listing the Python dependencies for the project.

## Author
Roee Bina





